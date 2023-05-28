import database.database as db
import database.food as tbl_food
import database.user as tbl_user
import database.record as tbl_record
import matplotlib.pyplot as plt

def get_top5_user():
    """Get numeric report about the top 5 users with the highest CO2 generation per day

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_user.get_top5_user(conn)

    print("--- TOP 5 USUARIO CON MAYOR EMISION DE CO2 POR DIA --")
    for idx, user in enumerate(data, start=1):
        print(f"***Top {idx}***")
        print(f"Identificacion: {user[0]}")
        print(f"Nombre: {user[1]}")
        print(f"Genero: {user[2]}")
        print(f"Emision de CO2 por dia: {user[3]:.3f}")
        print("")
    input("Presiona cualquier tecla para continuar...")
    print("")


def get_top5_food():
    """Get numeric report about the top 5 foods with the highest CO2 generation

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_food.get_all_foods(conn)[:5]

    print("--- TOP 5 COMIDAS CON MAYOR EMISION DE CO2 --")
    for idx, food in enumerate(data, start=1):
        print(f"***Top {idx}***")
        print(f"ID: {food[0]}")
        print(f"Nombre: {food[1]}")
        print(f"Emision de CO2: {food[2]:.3f}")
        print("")
    input("Presiona cualquier tecla para continuar...")
    print("")
    
def get_highest_co2_emmission_by_gender():
    """Get graphic report about the highest co2 emmission by gender

    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_record.get_highest_co2_emmission_by_gender(conn)
    total = data[0][1] + data[1][1]

    x = ()
    y = ()
    
    for gender, emmission in data:
        x += (gender, )
        y += (emmission/total, )
    
    plt.title("Porcentaje de emision de CO2 por genero")
    plt.pie(y, labels=x, autopct="%0.1f %%")
    plt.axis("equal")
    plt.show()

def get_top_food_graph():
    """Get graphic report about the top foods with the highest CO2 generation
    Returns
    -------
        None
    """
    conn = db.create_connection()
    data = tbl_food.get_all_foods(conn)[:10]
    
    x = ()
    y = ()

    for food in data:
        x += (food[2], )
        y += (food[1].capitalize(), )
    
    plt.title("Alimentos con mayor generacion de CO2")
    plt.xlabel("CO2 generado")
    plt.ylabel("Alimentos")
    plt.barh(y, x)
    plt.show()
