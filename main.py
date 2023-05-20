import database.database as database
import menu.menu as menu

def main():
    conn = database.create_connection()
    database.create_tables(conn)



if __name__ == '__main__':
    main()
