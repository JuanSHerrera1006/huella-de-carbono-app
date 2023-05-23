import utils.validations as validations 
import utils.images as img_functions
import utils.csv as csv_functions
import utils.format as formats
import utils.path as path_functions
import constants.constants as constants
import database.food as tbl_food
import database.database as db
import datetime

def register_food():
    """Register new food controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    name = input("Escriba el nombre de la comida a registrar: ").upper()
    co2_emmission = validations.real_input("Ingrese el nivel de CO2 generado por kg: ", 0, float('inf'))

    # Save in the database
    id_food = tbl_food.add_food(conn, name, co2_emmission)

    print("Se ha registrado el alimento correctamente en la base de datos")
    input("Presione cualquier tecla para continuar...")
    print("")

    opt = validations.char_input("¿Deseas ingresar un imagen Y/N ?: ", ["Y", "N"])

    if opt == "Y":
        ext, image_bytes = img_functions.image2blob()
        img_name = f"{name}_{id_food}{ext}"
        tbl_food.add_food_img(conn, id_food, image_bytes, img_name, ext)

        img = img_functions.blob2image(image_bytes)
        img_functions.save_image(img, img_name)

        print("Se ha registrado la imagen del alimento correctamente en la base de datos")
        input("Presione cualquier tecla para continuar...")
        print("")

    # Close connection
    conn.close()

def show_all_foods():
    """Show all foods controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_food.get_all_foods(conn)
    n = len(data)

    if n == 0:
        print("No se encuentra ningun alimento registrado")
        input("Presione cualquier tecla para continuar...")
        print("")
        return

    final_data = formats.list_any2list_str(data)
    print("")
    formats.show_list(final_data)

    opt = validations.char_input("¿Deseas saber mas informacion de algun alimento Y/N ?: ", ["Y", "N"])

    if opt == "Y":        
        idx = validations.integer_input("Digite el indice del alimento que desea conocer mas informacion: ", 1, n)
        selected_food = final_data[idx - 1]
        id_food = int(selected_food[0])
        
        print("")
        formats.show_table([selected_food], constants.HEADER_FOOD_TABLE)
        print("")

        img_meta_data = tbl_food.get_img_food_by_id(conn, id_food)
        
        if len(img_meta_data) == 0:
            print("No se encuentra ninguna imagen registrada para el alimento")
            input("Presione cualquier tecla para continuar...")
            print("")
        else:
            img_name = img_meta_data[0][0]
            img_path = f".\\assets\\images\\{img_name}"
            
            if not(path_functions.path_exists(img_path)):
                full_image_data = tbl_food.get_img_food_by_id(conn, id_food, False)
                image_bytes = full_image_data[0][1]
                img = img_functions.blob2image(image_bytes)
                # Save the image in the path
                img_functions.save_image(img, img_name)

            print("Se mostrara la imagen del alimento")
            input("Presione cualquier tecla para continuar...")
            print("")
            img_functions.show_image(img_name)
    # Close connection
    conn.close()

def del_food():
    """Delete food controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_food.get_all_foods(conn)
    n = len(data)

    if n == 0:
        print("No se encuentra ningun alimento registrado")
        input("Presione cualquier tecla para continuar...")
        print()
        return

    print("")
    final_data = formats.list_any2list_str(data)
    formats.show_list(final_data)
    idx = validations.integer_input("Ingrese el indice del alimento a eliminar: ", 1, n)
    selected_food = final_data[idx - 1]
 
    print("** Se eliminara el alimento con la siguiente informacion ***")

    print("")
    formats.show_table([selected_food], constants.HEADER_FOOD_TABLE)
    print("")

    opt = validations.char_input("¿Estas seguro de continuar con la operacion Y/N ?: ", ["Y", "N"])

    # Finish the process
    if opt == "N":
        return

    id_food = int(selected_food[0])
    food_name = selected_food[1]

    img_meta_data = tbl_food.get_img_food_by_id(conn, id_food)
        
    if len(img_meta_data) != 0:
        img_name = img_meta_data[0][0]
        img_path = f".\\assets\\images\\{img_name}"
        
        if path_functions.path_exists(img_path):
            # Remove the image 
            path_functions.remove_file(img_path)

    # Delete the food
    tbl_food.del_food_by_id(conn, id_food)
    print(f"Se ha eliminado el alimento \"{food_name}\" exitosamente")
    input("Presione cualquier tecla para continuar...")
    print("")

    # Close connection
    conn.close()


def create_csv_file():
    """Create csv with all foods data controller

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_food.get_all_foods(conn)

    if len(data) == 0:
        print("No se encuentra ningun alimento registrado")
        input("Presione cualquier tecla para continuar...")
        print()
        return
    
    today = datetime.date.today()
    file_name = f'foods_{today}.csv'

    csv_functions.create_csv(file_name, constants.HEADER_FOOD_TABLE, data)
    print(f"Se ha almacenado exitosamente el archivo en ROOT_DIR\\csv_data\\{file_name}")
    input("Presiona cualquier tecla para continuar...")
    print("")

    # Close connection
    conn.close()


