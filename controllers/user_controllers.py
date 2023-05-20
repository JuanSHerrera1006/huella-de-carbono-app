import constants.constants as constants
from sqlite3 import Connection
from typing import Any


def get_all_user(connection : Connection) -> list[Any]:
    """Get all the users registered in the database

    Parameters
    ----------
        connection: Connection
            The connection with the database

    Returns
    -------
        users: list[Any]
            List with the users registered in the database. Return an empty list if the query failed
    """
    users = [] 
    with connection:
        try:
            cur = connection.cursor()
            users = cur.execute(constants.GET_ALL_USERS).fetchall()
        except ValueError as e:
            print(e)
    return users
        
