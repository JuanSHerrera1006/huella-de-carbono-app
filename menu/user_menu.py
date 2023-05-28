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
    4) Actualizar un campo de un usuario
    5) Eliminar un usuario
    6) Crear archivo .csv
    7) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '7':
        if userInput == '1':
            controller.register_user()
        elif userInput == '2':
            controller.show_user_by_id()
        elif userInput == '3':
            controller.show_all_users()
        elif userInput == '4':
            submenu_user_update()
        elif userInput == '5':
            controller.del_user()
        elif userInput == '6':
           controller.create_csv_file()
        else:
            print('Has ingresado una opcion no valida')


def submenu_user_update():
    """App submenu user to update the fields
    
    Returns
    -------
        None
    """
    
    MENU_PROMPT = """--- ACTUALIZACION DE CAMPOS ---
    Selecciona el campo que deseas actualizar:

    1) Nombre
    2) Genero 
    3) Lugar de nacimiento
    4) Lugar de residencia
    5) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '5':
        if userInput == '1':
            controller.update_user_by_id("name")
        elif userInput == '2':
            controller.update_user_by_id("gender")
        elif userInput == '3':
            controller.update_user_by_id("place_of_birth")
        elif userInput == '4':
            controller.update_user_by_id("place_of_residence")
        else:
            print('Has ingresado una opcion no valida')

