import database.user as tbl_user
import database.database as db
import constants.constants as constants
import utils.csv as csv
import utils.format as formats
import utils.validations as validations
import datetime as datetime

def register_user(): 
    """Register new user controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    while True:
        reference = validations.numeric_input("Digite la identificacion del usuario: ")
        user = tbl_user.get_user_by_id(conn, reference)
        # Valid if the user exists
        if len(user) == 0:
            break
        # Show messages if user exists
        print("Ya se encuentra un usuario registrado con esta identificacion")
        print("Digite la identificacion nuevamente")
        input("Presione cualquier tecla para continuar...")
        print()
    
    name = input("Ingrese el nombre del usuario: ").upper()
    gender = validations.char_input("Ingrese el sexo del usuario M/F: ") 
    place_of_birth = input("Ingrese el lugar de nacimiento del usuario: ").upper()
    place_of_residence = input("Ingrese el lugar de residencia del usuario: ").upper()

    # Save in the database
    tbl_user.add_user(conn, reference, name, gender, place_of_birth, place_of_residence)
    print("Se ha registrado el usuario correctamente en la base de datos")
    input("Presione cualquier tecla para continuar...")
    print("")

    # Close connection 
    conn.close()
        
def show_user_by_id():
    """Show user by id (type table) controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    reference = input("Ingrese la identificacion del usuario a buscar: ")
    data = tbl_user.get_user_by_id(conn, reference)

    if len(data) == 0:
        print("No se encuentra ningun usuario registrado con esa identificacion")
        input("Presione cualquier tecla para continuar...")
        print()
        return
    
    print("")
    formats.show_table(data, constants.HEADER_USER_TABLE)
    print("")
    
    input("Presione cualquier tecla para continuar...")
    print("")
    # Close connection
    conn.close()

def show_all_users():
    """Show all users (type table) controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_user.get_all_user(conn)

    if len(data) == 0:
        print("No se encuentra ningun usuario registrado")
        input("Presione cualquier tecla para continuar...")
        print("")
        return

    print("")
    formats.show_table(data, constants.HEADER_USER_TABLE)
    print("")
    
    input("Presione cualquier tecla para continuar...")
    print("")
    # Close connection
    conn.close()


def update_user_by_id(field):
    # Create connection
    conn = db.create_connection()
    reference = input("Ingrese la identificacion del usuario a actualizar: ")
    data = tbl_user.get_user_by_id(conn, reference)

    if len(data) == 0:
        print("No se encuentra ningun usuario registrado con esa identificacion")
        input("Presione cualquier tecla para continuar...")
        print()
        return
    
    if field == constants.FIELDS_USER_TABLE["name"]:
        # If the field is name
        value = input("Ingrese el nuevo nombre del usuario: ").upper()
    elif field == constants.FIELDS_USER_TABLE["gender"]:
        # If the field is gender
        value = validations.char_input("Ingrese el nuevo sexo del usuario: ")
    elif field == constants.FIELDS_USER_TABLE["place_of_birth"]:
        # If the field is place_of_birth
        value = input("Ingrese el nuevo lugar de nacimiento del usuario: ").upper()
    elif field == constants.FIELDS_USER_TABLE["place_of_residence"]:
        # If the field is place_of_residence
        value = input("Ingrese el nuevo lugar de residencia del usuario: ").upper()
    else:
        # If the field doesn't exist
        print("Se ha enviado un campo no valido")
        input("Presione cualquier tecla para continuar...")
        print()
        return

    tbl_user.update_user_by_id(conn, field, value, reference)
    updated_user = tbl_user.get_user_by_id(conn, reference)
    
    print("")
    formats.show_table(updated_user, constants.HEADER_USER_TABLE)
    print("")

    input("Presione cualquier tecla para continuar...")
    print()




def del_user():
    """Delete user controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_user.get_all_user(conn)
    n = len(data)

    if n == 0:
        print("No se encuentra ningun usuario registrado")
        input("Presione cualquier tecla para continuar...")
        print()
        return

    print("--- Usuarios registrados actualmente ---")
    formats.show_list(data)
    idx = validations.integer_input("Ingrese el indice del usuario a eliminar: ", 1, n)
    selected_user = data[idx - 1]
 
    print("** Se eliminara el usuario con la siguiente informacion ***")

    print("")
    formats.show_table([selected_user], constants.HEADER_USER_TABLE)
    print("")

    opt = validations.char_input("¿Estas seguro de continuar con la operacion Y/N ?: ", ["Y", "N"])

    # Finish the process
    if opt == "N":
        return

    reference = selected_user[0]

    # Delete the user
    tbl_user.del_user_by_id(conn, reference)
    print(f"Se ha eliminado el usuario con id {reference} exitosamente")
    input("Presione cualquier tecla para continuar...")
    print("")

    # Close connection
    conn.close()



def create_csv_file():
    """Create csv with all users data controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_user.get_all_user(conn)

    if len(data) == 0:
        print("No se encuentra ningun usuario registrado")
        input("Presione cualquier tecla para continuar...")
        print()
        return
    
    today = datetime.date.today()
    file_name = f'users_{today}.csv'

    csv.create_csv(file_name, constants.HEADER_USER_TABLE, data)
    print(f"Se ha almacenado exitosamente el archivo en ROOT_DIR\\csv_data\\{file_name}")
    input("Presiona cualquier tecla para continuar...")
    print("")

    # Close connection
    conn.close()


