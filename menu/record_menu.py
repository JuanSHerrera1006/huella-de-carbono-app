import controllers.record_controllers as controller

def menu():
    """App menu about feeding records
    
    Returns
    -------
        None
    """
    
    MENU_PROMPT = """--- Registros de alimentacion ---
    Opciones:

    1) Crear un registro
    2) Ver todos los registros de un usuario
    3) Actualizar un registro
    4) Eliminar un registro
    5) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '5':
        if userInput == '1':
            controller.register_record()
        elif userInput == '2':
            controller.show_record()
        elif userInput == '3':
            controller.update_record()
        elif userInput == '4':
            controller.del_record()
        else:
            print('Has ingresado una opcion no valida')


