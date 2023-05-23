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
    3) Eliminar un alimento
    4) Crear archivo .csv
    5) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '5':
        if userInput == '1':
            controller.register_food()
        elif userInput == '2':
            controller.show_all_foods()
        elif userInput == '3':
            controller.del_food()
        elif userInput == '4':
            controller.create_csv_file()
        else:
            print('Has ingresado una opcion no valida')
