import menu.user_menu as user_menu
import menu.food_menu as food_menu

def menu() -> None:
    """App main menu
    
    Returns
    -------
        None
    """
    
    MENU_PROMPT = """--- MENU PRINCIPAL ---
    Opciones:

    1) Usuarios
    2) Alimentos
    3) Option 3
    4) Option 4
    5) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '5':
        if userInput == '1':
            user_menu.menu()
        elif userInput == '2':
            food_menu.menu()
        elif userInput == '3':
            pass
        elif userInput == '4':
            pass
        else:
            print('Has ingresado una opcion no valida')
