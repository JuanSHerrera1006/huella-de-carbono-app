import database.food as tbl_food
import utils.format as formats
import utils.validations as validations
import database.database as db

def calculator():
    """The CO2 calculator. Calculate the kgs per day of co2 

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_food.get_all_foods(conn)
    n = len(data)

    if n == 0:
        print("No se encuentra ningun alimento registrado")
        input("Presione cualquier tecla para continuar...")
        print("")
        return

    print("--- Alimentos registrados actualmente ---")
    final_data = formats.list_any2list_str(data)
    print("")
    formats.show_list(final_data)

    idx = validations.integer_input("Digite el indice del alimento que desea seleccionar: ", 1, n)
    selected_food = final_data[idx - 1]
    food_name = selected_food[1]
    co2_emmission = float(selected_food[2])
    days = validations.integer_input("Ingrese el numero de veces que come el alimento por dia: ", 0, float('inf'))
    
    print("")
    print("--- Resultados ---")
    print(f"Generas {co2_emmission * days} kgs de CO2 por dia al consumir el alimento \"{food_name}\"")
    input("Presiona cualquier tecla para continuar...")
    print("")
    


