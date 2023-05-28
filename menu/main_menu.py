import menu.food_menu as food_menu
import menu.user_menu as user_menu
import menu.record_menu as record_menu
import utils.co2_calculator as co2_calculator
import database.database as database

def menu():
    """App main menu
    
    Returns
    -------
        None
    """
    
    MENU_PROMPT = """--- MENU PRINCIPAL ---
    Opciones:

    1) Usuarios
    2) Alimentos
    3) Registros de alimentacion
    4) Calculadora de Co2
    5) Informes
    6) Crear copia de seguridad
    7) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '7':
        if userInput == '1':
            user_menu.menu()
        elif userInput == '2':
            food_menu.menu()
        elif userInput == '3':
            record_menu.menu() 
        elif userInput == '4':
            co2_calculator.calculator()
        elif userInput == '5':
            pass
        elif userInput == '6':
            database.create_backup()
        else:
            print('Has ingresado una opcion no valida')
