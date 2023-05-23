# Database name
DB_NAME = "./co2_emmissions.db"

#Filetypes
IMAGES_FILETYPES = [("Archivos de imagenes", ".jpeg .jpg .png")]

# Header food table
HEADER_FOOD_TABLE = ("id", "name", "co2_emmission", "create_at")

# Header user table
HEADER_USER_TABLE = ("reference", "name", "gender", "place_of_birth", "place_of_residence", "create_at")

# Create food table SQL
CREATE_FOOD_TABLE = """
CREATE TABLE IF NOT EXISTS food(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL, 
    co2_emmission FLOAT NOT NULL,
    create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""

# Create user table SQL
CREATE_USER_TABLE = """
CREATE TABLE IF NOT EXISTS user(
    reference TEXT PRIMARY KEY NOT NULL, 
    name TEXT NOT NULL, 
    gender TEXT NOT NULL, 
    place_of_birth TEXT NOT NULL, 
    place_of_residence TEXT NOT NULL, 
    create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
""" 

# Create record table (userxfood) SQL
CREATE_USERXFOOD_TABLE = """
CREATE TABLE IF NOT EXISTS record(
    id_food INTEGER NOT NULL, 
    id_user TEXT NOT NULL, 
    kg_per_day FLOAT NOT NULL,
    PRIMARY KEY(id_food, id_user)
    FOREIGN KEY(id_food) 
        REFERENCES food(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(id_user) 
        REFERENCES user(reference)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

CREATE_IMAGE_TABLE = """
CREATE TABLE IF NOT EXISTS image(
    id_food INTEGER NOT NULL,
    image BLOB NOT NULL,
    name TEXT NOT NULL,
    format TEXT NOT NULL,
    PRIMARY KEY(id_food),
    FOREIGN KEY(id_food) 
        REFERENCES food(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

# Query to get all foods
GET_ALL_FOODS = "SELECT * FROM food ORDER BY id ASC;"

# Query to get all users
GET_ALL_USERS = "SELECT * FROM user ORDER BY reference ASC;"

# Query to delete user
DEL_USER_BY_ID = "DELETE FROM user WHERE reference = ?"

# Query to delete food
DEL_FOOD_BY_ID = "DELETE FROM food WHERE id = ?"

# Query to get user by id
GET_USER_BY_ID = "SELECT * FROM user WHERE reference = ?"

# Query to get name image by id_food
GET_IMAGE_NAME_BY_ID = "SELECT name FROM image WHERE id_food = ?"

# Query to get image by id_food
GET_IMAGE_BY_ID = "SELECT * FROM image WHERE id_food = ?"

# Query to insert a food in the table "food"
INSERT_FOOD = "INSERT INTO food(name, co2_emmission) VALUES (?, ?);" 

# Query to insert a food image in the table "image"
INSERT_FOOD_IMG = "INSERT INTO image(id_food, image, name, format) VALUES (?, ?, ?, ?)"

# Query to insert a user in the table "user"
INSERT_USER = """
INSERT INTO user(reference, name, gender, place_of_birth, place_of_residence)
VALUES
(?, ?, ?, ?, ?);
"""

