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

def add_food(connection : Connection, name: str, co2_emmission: float) -> None:
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
        None
    """
    with connection:
        try:
            cur = connection.cursor()
            params = (name, co2_emmission)
            cur.execute(constants.INSERT_FOOD, params)
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)


