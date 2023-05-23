import menu.user_menu as user_menu
import menu.food_menu as food_menu
import utils.co2_calculator as co2_calculator
import database.database as database

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
    3) Calculadora de Co2
    4) Informes
    5) Crear copia de seguridad
    6) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '6':
        if userInput == '1':
            user_menu.menu()
        elif userInput == '2':
            food_menu.menu()
        elif userInput == '3':
            co2_calculator.calculator()
        elif userInput == '4':
            pass
        elif userInput == '5':
            database.create_backup()
        else:
            print('Has ingresado una opcion no valida')
