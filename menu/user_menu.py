import controllers.user_controllers as controller

def menu():
    """App user menu
    
    Returns
    -------
        None
    """
    
    MENU_PROMPT = """--- ADMINISTRADOR DE USUARIO ---
    Opciones:

    1) Registrar un nuevo usuario
    2) Buscar un usuario por ID
    3) Listar todos los usuarios
    4) Eliminar un usuario
    5) Crear archivo .csv
    6) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '6':
        if userInput == '1':
            controller.register_user()
        elif userInput == '2':
            controller.show_user_by_id()
        elif userInput == '3':
            controller.show_all_users()
        elif userInput == '4':
            controller.del_user()
        elif userInput == '5':
            controller.create_csv_file()
        else:
            print('Has ingresado una opcion no valida')

