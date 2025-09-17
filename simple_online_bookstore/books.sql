DROP TABLE IF EXISTS books;

CREATE TABLE books
(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    type TEXT,
    img_loc TEXT,
    stockpiles NOT NULL   
);

INSERT INTO books (name, price, description, type, img_loc, stockpiles)
VALUES
    ('The Three-Body Problem I',10.3,'"The Three-Body Problem" is a science fiction novel by Chinese author Liu Cixin, and its the first book in the "Remembrance of Earths Past" trilogy. The story begins during Chinese Cultural Revolution and unfolds into a complex narrative involving a secret military project, the search for extraterrestrial intelligence, and the subsequent contact with an alien civilization from the Alpha Centauri star system. This civilization is facing the destruction of their own planet and sees Earth as a potential new home. The novel combines hard science fiction with deep philosophical questions, exploring themes of communication, humanity place in the universe, and the consequences of first contact.','science fiction','Threebody.jpg',100),
    ('Dune',10.1,'"Dune" by Frank Herbert is a seminal science fiction novel that stands at the crossroads of adventure, mysticism, politics, and ecology. Set in the distant future within a feudal interstellar society, it tells the story of young Paul Atreides, whose family accepts stewardship of the desert planet Arrakis. As the only source of the universes most valuable substance, the spice Melange, which grants psychic abilities and extended life, Arrakis is a contested land. Pauls journey is one of revenge, political intrigue, and spiritual awakening, set against the backdrop of a harsh desert landscape, populated by giant sandworms and fierce natives. "Dune" explores themes of power, religion, and human nature, creating a universe that has captivated readers for decades.','science fiction','Dune.jpg',100),
    ('Pride and Prejudice',30.3,'"Pride and Prejudice" by Jane Austen is a timeless novel that explores the tumultuous relationship between Elizabeth Bennet, a spirited and intelligent young woman, and Fitzwilliam Darcy, a wealthy, proud man. Set in rural England in the early 19th century, it delves into themes of marriage, social class, and personal growth. Through witty dialogue and a cast of memorable characters, Austen critiques the societal norms of her time, while weaving a captivating love story that examines the fine line between pride and prejudice.','romantic','prideandprejudice.jpg',100),
    ('Romeo and Juliet',14.3,'"Romeo and Juliet" by William Shakespeare is a tragic romance that unfolds in the city of Verona, where two young lovers from feuding families fall passionately in love. Their ill-fated relationship is marked by impulsive decisions and a cruel twist of fate, leading to a devastating conclusion. Shakespeares play explores themes of love, fate, and the destructive power of familial conflict. Through beautiful language and intense emotion, it captures the exhilaration and tragedy of first love, making it one of the most enduring love stories in literature.','romantic','Romeo_and_juliet.jpg',100),
    ('The Hunchback of Notre-Dame',110.3,'"The Hunchback of Notre-Dame" is a historical novel by Victor Hugo, set in 15th-century Paris. It tells the tragic story of Quasimodo, the deformed bell ringer of Notre Dame, and his unrequited love for the beautiful gypsy, Esmeralda. Against a backdrop of Gothic architecture and medieval Paris, Hugo weaves a compelling narrative of love, betrayal, and redemption. Through its vivid characters, the novel explores themes of societal exclusion and the human desire for acceptance and love. Hugy masterpiece not only offers a critical view of society moral hypocrisy but also celebrates the resilience of the human spirit.','historical','Notre_Dame.jpg',100),
    ('Les Misérables',140.3,'"Les Misérables" is a monumental novel by Victor Hugo, set against the backdrop of 19th-century France. It intricately weaves the lives of characters struggling with injustice, love, and redemption. At its heart is Jean Valjean, a former convict whose attempts to rebuild his life are constantly threatened by his past. Alongside him are characters like the noble Marius, the tragic Fantine, and the relentless Inspector Javert, each exploring themes of morality, society, and the nature of freedom. Hugo epic tale is a profound commentary on the human condition, highlighting the endurance of spirit amidst adversity and the transformative power of compassion.','historical','Ebcosette.jpg',100);

DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY,
    password TEXT NOT NULL
);
