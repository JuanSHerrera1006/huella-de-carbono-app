import database.database as db
import constants.constants as constants
import utils.validations as validations
import utils.format as formats
import utils.csv as csv_functions
import database.record as tbl_record
import database.user as tbl_user
import database.food as tbl_food
import datetime

def register_record():
    """Register new record controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    reference = input("Escriba el documento del usuario que desea crear registro de alimentacion: ")
    user_data = tbl_user.get_user_by_id(conn, reference)

    if len(user_data) == 0:
        print("No se encuentra ningun usuario registrado con esa identificacion")
        input("Presione cualquier tecla para continuar...")
        print()
        return

    food_data = tbl_food.get_all_foods(conn)

    if len(food_data) == 0:
        print("No se encuentra ningun alimento registrado")
        input("Presione cualquier tecla para continuar...")
        print("")
        return

    final_data = formats.list_any2list_str(food_data)
    print("--- Alimentos registrados actualmente ---")
    formats.show_list(final_data)

    idx = validations.integer_input("Digite el indice del alimento del cual desea crear un registro: ", 1, len(food_data))
    selected_food = final_data[idx - 1]
    id_food = int(selected_food[0])

    record = tbl_record.get_record(conn, reference, id_food)

    if len(record) != 0:
        print(f"Ya se encuentra un registro de este alimento para el usuario con ID: {reference}")
        input("Presione cualquier tecla para continuar...")
        print("")
        return

    consumption_per_day = validations.integer_input("Ingrese el numero de consumos por dia del alimento: ", 0, float('inf'))

    tbl_record.add_record(conn, reference, id_food, consumption_per_day)

    # Close connection
    conn.close()

def show_record():
    """Show record controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    reference = input("Escriba el documento del usuario que desea visualizar los registros de alimentacion: ")
    user_data = tbl_user.get_user_by_id(conn, reference)

    if len(user_data) == 0:
        print("No se encuentra ningun usuario registrado con esa identificacion")
        input("Presione cualquier tecla para continuar...")
        print()
        return
    
    data = tbl_record.get_records_by_reference(conn, reference)
    final_data = formats.list_any2list_str(data)
    print("")
    formats.show_table(final_data, constants.HEADER_RECORD_TABLE)
    print("")

def update_record():
    """Update record controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    reference = input("Escriba el documento del usuario que le desea actualizar un registro de alimentacion: ")
    user_data = tbl_user.get_user_by_id(conn, reference)

    if len(user_data) == 0:
        print("No se encuentra ningun usuario registrado con esa identificacion")
        input("Presione cualquier tecla para continuar...")
        print()
        return

    data = tbl_record.get_records_by_reference(conn, reference)
    final_data = formats.list_any2list_str(data)
    if len(data) == 0:
        print("No se encuentra ningun registro de alimentacion del usuario")
        input("Presione cualquier tecla para continuar...")
        print("")
        return

    print("--- Alimentos registrados actualmente ---")
    formats.show_list(final_data)

    idx = validations.integer_input("Digite el indice del alimento que desea actualizar de su registro de alimentacion: ", 1, len(data))
    selected_food = final_data[idx - 1]
    id_food = int(selected_food[0])

    consumption_per_day = validations.integer_input("Ingrese el nuevo consumo por dia del usuario: ", 0, float('inf'))
    tbl_record.update_record(conn, reference, id_food, consumption_per_day)
    record = tbl_record.get_record(conn, reference, id_food)
    final_record = formats.list_any2list_str(record)

    print("Dato actualizado correctamente ")

    print("")
    formats.show_table(final_record, constants.HEADER_RECORD_TABLE)
    print("")

    input("Presione cualquier tecla para continuar...")
    print("")

    # Close connection
    conn.close()

def del_record():
    """Delete record controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    reference = input("Escriba el documento del usuario que le desea eliminar un registro de alimentacion: ")
    user_data = tbl_user.get_user_by_id(conn, reference)

    if len(user_data) == 0:
        print("No se encuentra ningun usuario registrado con esa identificacion")
        input("Presione cualquier tecla para continuar...")
        print()
        return

    data = tbl_record.get_records_by_reference(conn, reference)
    final_data = formats.list_any2list_str(data)

    if len(data) == 0:
        print("No se encuentra ningun registro de alimentacion del usuario")
        input("Presione cualquier tecla para continuar...")
        print("")
        return

    print("--- Alimentos registrados actualmente ---")
    formats.show_list(final_data)

    idx = validations.integer_input("Digite el indice del alimento que desea eliminar de su registro de alimentacion: ", 1, len(data))
    selected_food = final_data[idx - 1]
    id_food = int(selected_food[0])
    
    record = tbl_record.get_record(conn, reference, id_food)
    final_record = formats.list_any2list_str(record)

    print("*** Se eliminara el siguiente registro de alimentacion ***")

    print("")
    formats.show_table(final_record, constants.HEADER_RECORD_TABLE)
    print("")

    opt = validations.char_input("¿Estas seguro de continuar con la operacion Y/N ?: ", ["Y", "N"])

    # Finish the process
    if opt == "N":
        return

    tbl_record.del_record(conn, reference, id_food)
    # Close connection
    conn.close()

def create_csv_file():
    """Create csv with all records data controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_record.get_all_records(conn)

    if len(data) == 0:
        print("No se encuentra ningun alimento registrado")
        input("Presione cualquier tecla para continuar...")
        print()
        return
    
    today = datetime.date.today()
    file_name = f'records_{today}.csv'

    csv_functions.create_csv(file_name, constants.HEADER_RECORD_INCLUDE_USER_TABLE, data)
    print(f"Se ha almacenado exitosamente el archivo en ROOT_DIR\\csv_data\\{file_name}")
    input("Presiona cualquier tecla para continuar...")
    print("")

    # Close connection
    conn.close()
