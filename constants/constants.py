# Database name
DB_NAME = "./co2_emmissions.db"

#Filetypes
IMAGES_FILETYPES = [("Archivos de imagenes", ".jpeg .jpg .png")]

# Header food table
HEADER_FOOD_TABLE = ("id", "name", "co2_emmission", "create_at")

# Header user table
HEADER_USER_TABLE = ("reference", "name", "gender", "place_of_birth", "place_of_residence", "create_at")

# Header record table
HEADER_RECORD_TABLE = ("id_food", "food_name", "co2_food_emmission", "consumption_per_day", "total_emmission")

# Header record table (include id_user)
HEADER_RECORD_INCLUDE_USER_TABLE = ("id_food", "id_user", "food_name", "co2_food_emmission", "consumption_per_day", "total_emmission")

# Fields food table
FIELDS_FOOD_TABLE = {
    "name": "name",
    "co2_emmission": "co2_emmission"
}

# Fields user table
FIELDS_USER_TABLE = {
        "name": "name",
        "gender": "gender",
        "place_of_birth": "place_of_birth",
        "place_of_residence": "place_of_residence"
}

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
    consumption_per_day INT NOT NULL,
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

# Create image table SQL
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
GET_ALL_FOODS = "SELECT * FROM food ORDER BY co2_emmission DESC;"

# Query to get all users
GET_ALL_USERS = "SELECT * FROM user ORDER BY reference ASC;"

# Query to delete user
DEL_USER_BY_ID = "DELETE FROM user WHERE reference = ?"

# Query to delete food
DEL_FOOD_BY_ID = "DELETE FROM food WHERE id = ?"

# Query to delete record
DEL_RECORD = "DELETE FROM record WHERE id_user = ? AND id_food = ?"

# Query to get user by id
GET_USER_BY_ID = "SELECT * FROM user WHERE reference = ?"

# Query to get name image by id_food
GET_IMAGE_NAME_BY_ID = "SELECT name FROM image WHERE id_food = ?"

# Query to get image by id_food
GET_IMAGE_BY_ID = "SELECT * FROM image WHERE id_food = ?"

# Query to get a record
GET_RECORD = """
SELECT 
    F.id,
    F.name,
    F.co2_emmission,
    R.consumption_per_day, 
    (F.co2_emmission * R.consumption_per_day) AS total_emmission
FROM record AS R
    INNER JOIN food AS F
        ON F.id = R.id_food
WHERE id_user = ? AND id_food = ?
"""

# Query to get all records
GET_ALL_RECORDS = """
SELECT 
    F.id,
    R.id_user,
    F.name,
    F.co2_emmission,
    R.consumption_per_day, 
    (F.co2_emmission * R.consumption_per_day) AS total_emmission
FROM record AS R
    INNER JOIN food AS F
        ON F.id = R.id_food
"""

# Query to get records by reference
GET_RECORDS_BY_REFERENCE = """
SELECT 
    F.id, 
    F.name,
    F.co2_emmission,
    R.consumption_per_day, 
    (F.co2_emmission * R.consumption_per_day) AS total_emmission
FROM record AS R
    INNER JOIN food AS F
        ON F.id = R.id_food
WHERE id_user = ?"""

# Query to insert a food in the table "food"
INSERT_FOOD = "INSERT INTO food(name, co2_emmission) VALUES (?, ?);" 

# Query to insert a food image in the table "image"
INSERT_FOOD_IMG = "INSERT INTO image(id_food, image, name, format) VALUES (?, ?, ?, ?)"

# Query to insert a record in the table "record"
INSERT_RECORD = "INSERT INTO record(id_user, id_food, consumption_per_day) VALUES (?, ?, ?)"

# Query to insert a user in the table "user"
INSERT_USER = """
INSERT INTO user(reference, name, gender, place_of_birth, place_of_residence)
VALUES
(?, ?, ?, ?, ?);
"""

# Query to update the user name by id
UPDATE_USER_NAME_BY_ID = "UPDATE user SET name = ? WHERE reference = ?"

# Query to update the user gender by id
UPDATE_USER_GENDER_BY_ID = "UPDATE user SET gender = ? WHERE reference = ?"

# Query to update the user place of birth by id
UPDATE_USER_PLACE_OF_BIRTH_BY_ID = "UPDATE user SET place_of_birth = ? WHERE reference = ?"

# Query to update the user place of residence by id
UPDATE_USER_PLACE_OF_RESIDENCE_BY_ID = "UPDATE user SET place_of_residence = ? WHERE reference = ?"

# Query to update the image food by ID food 
UPDATE_IMAGE_BY_FOOD_ID = "UPDATE image SET image = ?, name = ?, format = ? WHERE id_food = ?"

# Query to update the food name by id
UPDATE_FOOD_NAME_BY_ID = "UPDATE food SET name = ? WHERE id = ?"

# Query to update the food co2 emmission by id
UPDATE_FOOD_CO2_EMMISSION_BY_ID = "UPDATE food SET co2_emmission = ? WHERE id = ?"

# Query to update the record consumption per day
UPDATE_RECORD_CONSUMPTION = "UPDATE record SET consumption_per_day = ? WHERE id_user = ? AND id_food = ?"

# Query to search top 5 users with the highest CO2 generation
GET_TOP5_USER = """
SELECT 
	U.reference,
	U.name,
	U.gender,
	SUM(F.co2_emmission * R.consumption_per_day) AS total_emmision
FROM record AS R	
    JOIN food AS F
        ON F.id = R.id_food
	JOIN user as U
		ON u.reference = R.id_user
GROUP BY U.reference
ORDER BY total_emmision DESC
LIMIT 5
"""

# Query to search highest CO2 generation by gender
GET_HIGHEST_CO2_EMMISSION_BY_GENDER = """
SELECT 
	U.gender,
	SUM(F.co2_emmission * R.consumption_per_day) AS total_emmision
FROM record AS R	
    JOIN food AS F
        ON F.id = R.id_food
	JOIN user as U
		ON u.reference = R.id_user
GROUP BY U.gender
"""
