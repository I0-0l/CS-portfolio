# admin account:
# user id :admin
#password: 001
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, session, redirect, url_for, g, request
from database import get_db, close_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm,UploadForm
from functools import wraps


app=Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "Ljn302212"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def load_logged_in_user():
    g.user = session.get("user_id",None)

def login_required(view):
    @wraps(view)
    def wrapped_view(*args,**kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(*args, **kwargs)
    return wrapped_view

@app.route("/")
@app.route("/home")
def books():
    db = get_db()
    books = db.execute("SELECT * FROM books;").fetchall()
    return render_template("home.html",books=books)

@app.route("/book/<book_type>")
def books_by_type(book_type):
    db = get_db()
    books = db.execute("""SELECT * FROM books
                         WHERE type = ?;""", (book_type,)).fetchall()
    return render_template("booktype.html",books=books)

@app.route("/book/<int:book_id>")
def book(book_id):
    db = get_db()
    book = db.execute("""SELECT * FROM books
                        WHERE book_id = ?;""", (book_id,)).fetchone()
    return render_template("book.html", book=book)    

@app.route("/cart")
@login_required
def cart():
    if "cart" not in session:
        session["cart"] = {}
    names = {}
    sum = 0
    db = get_db()
    for book_id in session["cart"]:
        books_details = {}
        book = db.execute("""SELECT * FROM books
                             Where book_id = ?;""",(book_id,)).fetchone()
        books_details["number"] = session["cart"][book_id]
        books_details["name"] = book["name"]
        books_details["price"] = book["price"]
        books_details["img_loc"] = book["img_loc"]
        books_details["price_total"] = round((book["price"] * session["cart"][book_id]),2)
        books_details["book_id"] = book["book_id"]
        sum += round((book["price"] * session["cart"][book_id]), 2)
        names[book_id] = books_details
    return render_template("cart.html",cart= session["cart"], names=names, sum=sum)

@app.route("/add_to_cart/<int:book_id>")
@login_required
def add_to_cart(book_id):
    if "cart" not in session:
        session["cart"] = {}
    if book_id not in session["cart"]:
        session["cart"][book_id] = 1
    else:
        session["cart"][book_id] = session["cart"][book_id] + 1 

    session.modified = True
    return redirect( url_for("cart") )

@app.route("/reduce_from_cart/<int:book_id>")
def reduce_from_cart(book_id):
    if session["cart"][book_id] == 1:
        session["cart"].pop(book_id)
    else:
        session["cart"][book_id] -= 1 
    session.modified = True
    return redirect( url_for("cart") )

@app.route("/add_in_cart/<int:book_id>")
def add_in_cart(book_id):
    session["cart"][book_id] += 1 
    session.modified = True
    return redirect( url_for("cart") )

@app.route("/add_into_stockpiles", methods=["GET","POST"])
def add_into_stockpiles():
    db = get_db()
    books = db.execute("SELECT * FROM books;").fetchall()
    form = UploadForm()
    if form.validate_on_submit():
        name = form.book_name.data
        price = float(form.price.data)
        description =form.description.data
        book_type = form.type.data
        stockpiles = form.stockpiles.data
        img_loc = form.img_loc.data
        file = form.book_cover.data
        print(file)
        db.execute("""INSERT INTO books(name, price, description, type, img_loc, stockpiles) 
                VALUES(?, ?, ?, ?, ?, ?);""",(name, price, description, book_type, img_loc, stockpiles,))
        db.commit()
        filename = form.img_loc.data
        form.book_cover.data.save(os.path.join( "static/", filename))        
    return render_template("Admin.html", form=form, books=books)

@app.route("/buy")
def buy():
    db = get_db()
    for book_id in session["cart"].keys():
        db.execute("""UPDATE books set stockpiles = stockpiles - ? 
                            where book_id = ?;""",(session["cart"][book_id], book_id,)).fetchone()
        db.commit()
    books = db.execute("SELECT * FROM books;").fetchall()
    session.pop("cart")
    return render_template("finished.html", books=books)

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        db= get_db()
        conflict_user = db.execute(
            """SELECT * FROM users
            Where user_id = ?;""", (user_id,)).fetchone()
        if conflict_user is not None:
            form.user_id.errors.append("User name already taken")
        else:
            db.execute("""
                INSERT INTO users (user_id, password)
                VALUES (?,?);""",
                (user_id, generate_password_hash(password)))
            db.commit()
            return redirect( url_for("login") )
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        db = get_db()
        user = db.execute(
            """SELECT * FROM users
                WHERE user_id = ?;""", (user_id,)).fetchone()
        if user is None:
            form.user_id.errors.append("User name not found")
        elif not check_password_hash(user["password"],password):
            form.password.errors.append("Incorrect password!")
        else:
            session.clear()
            session["user_id"] = user_id 
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("books")
            return redirect(next_page)
    return render_template("login.html",form=form)
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("books"))