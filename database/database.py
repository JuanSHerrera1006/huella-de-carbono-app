import constants.constants as constants
import utils.path as path_functions
import datetime as datetime
from sqlite3 import connect
import io
import os

def create_connection():
    """Returns the database connection 
 
    Returns
    -------
        connection : Connection
            Connection to database
    """
    return connect(constants.DB_NAME)

def create_tables(connection):
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

def create_backup():
    """Create backup of the db
        
    Returns
    -------
        None
    """
    connection = create_connection()
    today = datetime.datetime.now()
    dt_string = today.strftime("%d-%m-%Y_%H-%M-%S")
    file_name = f"backup_{dt_string}.sql"
    ROOT_PATH = path_functions.get_root_dir()
    DEST_PATH = ".\\backup\\" + file_name
    FILE_PATH = os.path.abspath(os.path.join(ROOT_PATH, DEST_PATH)) 

    with io.open(FILE_PATH, "w") as file:
        for data in connection.iterdump():
            file.write(f"{data}\n")

    print("Se ha creado correctamente la copia de seguridad de la base de datos")
    input("Presiona cualquier tecla para continuar...")
    print("")
    # Close connection
    connection.close()


