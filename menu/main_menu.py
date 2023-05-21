def menu() -> None:
    """App main menu
    
    Returns
    -------
        None
    """
    
    MENU_PROMPT = """--- MENU PRINCIPAL ---
    Opciones:

    1) Option 1
    2) Option 2
    3) Option 3
    4) Option 4
    5) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '5':
        if userInput == '1':
            pass
        elif userInput == '2':
            pass
        elif userInput == '3':
            pass
        elif userInput == '4':
            pass
        else:
            print('Has ingresado una opcion no valida')

