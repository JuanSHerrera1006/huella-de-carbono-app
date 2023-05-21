# Database name
DB_NAME = "./co2_emmissions.db"

#Filetypes
IMAGES_FILETYPES = [("Archivos de imagenes", ".jpeg .jpg .png")]

# Header food table
HEADER_FOOD_TABLE = ("id", "nombre", "co2_emmission", "create_at")

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
    FOREIGN KEY(id_food) REFERENCES food(id),
    FOREIGN KEY(id_user) REFERENCES user(reference),
    PRIMARY KEY(id_food, id_user)
    );
"""

CREATE_IMAGE_TABLE = """
CREATE TABLE IF NOT EXISTS image(
    id_food INTEGER NOT NULL,
    image BLOB NOT NULL,
    name TEXT NOT NULL,
    format TEXT NOT NULL,
    FOREIGN KEY(id_food) REFERENCES food(id),
    PRIMARY KEY(id_food)
)
"""

# Query to get all foods
GET_ALL_FOODS = "SELECT * FROM food"

# Query to get all users
GET_ALL_USERS = "SELECT * FROM user"

# Query to insert a food in the table "food"
INSERT_FOOD = "INSERT INTO food(name, co2_emmission) VALUES (?, ?)" 


