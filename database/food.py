import constants.constants as constants
from sqlite3 import Connection
from typing import Any


def get_all_foods(connection : Connection) -> list[Any]:
    """Get all the foods registered in the database

    Parameters
    ----------
        connection: Connection
            The connection with the database

    Returns
    -------
        foods: list[Any]
            List with the foods registered in the database. Return an empty list if the query failed
    """
    foods = [] 
    with connection:
        try:
            cur = connection.cursor()
            foods = cur.execute(constants.GET_ALL_FOODS).fetchall()
        except ValueError as e:
            print(e)
    return foods

def get_img_food_by_id(connection : Connection, id_food : int, only_meta_data : bool = True) -> list[Any]:
    """Get all the foods registered in the database

    Parameters
    ----------
        connection: Connection
            The connection with the database

    Returns
    -------
        foods: list[Any]
            List with the foods registered in the database. Return an empty list if the query failed
    """
    image = [] 
    with connection:
        try:
            cur = connection.cursor()
            if only_meta_data:
                image = cur.execute(constants.GET_IMAGE_NAME_BY_ID, (id_food, )).fetchall()
            else:
                image = cur.execute(constants.GET_IMAGE_BY_ID, (id_food, )).fetchall()
        except ValueError as e:
            print(e)
    return image


def add_food(connection : Connection, name: str, co2_emmission: float) -> int | None:
    """Insert a new register in the table "food"

    Parameters
    ----------
        connection: Connection
            The connection with the database
        name: str
            The food name to be register
        co2_emmission: float
            The co2 emmision per kg

    Returns
    -------
        id_food: int | None
            Return the registered food id
    """
    with connection:
        id_food = -1
        try:
            cur = connection.cursor()
            params = (name, co2_emmission)
            cur.execute(constants.INSERT_FOOD, params)
            # Save the changes in the database
            connection.commit()
            # Get the id 
            id_food = cur.lastrowid
            # Close the cursor
            cur.close()
            return id_food
        except ValueError as e:
            print(e)

def add_food_img(connection : Connection, id_food: int | None, image: bytes, name: str, format_img: str) -> None:
    """Insert a new register in the table "food"

    Parameters
    ----------
        connection: Connection
            The connection with the database
        id_food : int
            The ID food to register the image
        image : bytes
            The image type bytes
        name: str
            The image name that it will be saving
        format_img: str
            The image format (.jpg, .jpeg, .png)
    Returns
    -------
        None
    """
    with connection:
        try:
            cur = connection.cursor()
            params = (id_food, image, name, format_img)
            cur.execute(constants.INSERT_FOOD_IMG, params)
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)

def del_food_by_id(connection : Connection, id_food: int) -> None:
    """Delete a food with the id_food choosed

    Parameters
    ----------
        connection : Connection
            The connection with the database
        id_food : str
            The ID of the food
    
    Returns
    -------
        None
    """
    with connection:
        try:
            cur = connection.cursor()
            cur.execute(constants.DEL_FOOD_BY_ID, (id_food, ))
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)

