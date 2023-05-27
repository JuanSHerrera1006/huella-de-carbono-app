import controllers.food_controllers as controller

def menu():
    """App food module menu
    
    Returns
    -------
        None
    """
    
    MENU_PROMPT = """--- ADMINISTRADOR DE ALIMENTOS --- 
    Opciones:
    1) Registrar un nuevo alimento
    2) Listar todos los alimentos
    3) Actualizar un alimento
    4) Eliminar un alimento
    5) Crear archivo .csv
    6) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '6':
        if userInput == '1':
            controller.register_food()
        elif userInput == '2':
            controller.show_all_foods()
        elif userInput == '3':
             submenu_food_update()
        elif userInput == '4':
            controller.del_food()
        elif userInput == '5':
            controller.create_csv_file()
        else:
            print('Has ingresado una opcion no valida')

def submenu_food_update():
    """App submenu food to update the fields
    
    Returns
    -------
        None
    """
    
    MENU_PROMPT = """--- ACTUALIZACION DE CAMPOS ---
    Selecciona el campo que deseas actualizar:

    1) Nombre
    2) Cantidad de co2 generado por kg 
    3) Imagen
    4) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '4':
        if userInput == '1':
            controller.update_food_by_id("name")
        elif userInput == '2':
            controller.update_food_by_id("co2_emmission")
        elif userInput == '3':
            controller.update_food_by_id("image")
        else:
            print('Has ingresado una opcion no valida')
