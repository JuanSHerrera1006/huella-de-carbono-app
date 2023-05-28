import utils.reports as reports

def menu():
    """App reports menu
    
    Returns
    -------
        None
    """
    
    MENU_PROMPT = """--- Informes ---
    Opciones:

    1) Top 5 usuarios con mayor generacion de CO2
    2) Top 5 alimento generadores de CO2
    3) Grafica alimentos generadores de CO2
    4) Grafica usuarios generadores de CO2 por genero
    5) Exit

    La opcion que has elegido es: """

    while (userInput := input(MENU_PROMPT)) != '5':
        if userInput == '1':
            reports.get_top5_user()
        elif userInput == '2':
            reports.get_top5_food()
        elif userInput == '3':
            reports.get_top_food_graph()
        elif userInput == '4':
            reports.get_highest_co2_emmission_by_gender()
        else:
            print('Has ingresado una opcion no valida')
