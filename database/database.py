import constants.constants as constants
from sqlite3 import connect, Connection

def create_connection() -> Connection:
    """Returns the database connection 
 
    Returns
    -------
        connection : Connection
            Connection to database
    """
    return connect(constants.DB_NAME)

def create_tables(connection : Connection) -> None:
    """Create all tables to the app 
 
    Parameters
    ----------
        connection : Connection 
            The connection with the database

    Returns
    -------
        None
    """
    with connection:
        tables_sql = (
            constants.CREATE_FOOD_TABLE,          
            constants.CREATE_USER_TABLE, 
            constants.CREATE_USERXFOOD_TABLE,
            constants.CREATE_IMAGE_TABLE
        )
        for query in tables_sql:
            connection.execute(query)
    print("*** Se ha creado exitosamente las tablas ***")


