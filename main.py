import database.database as database
import menu.main_menu as menu

def main():
    conn = database.create_connection()
    # Create tables
    database.create_tables(conn)
    # Close connection
    conn.close()
    # Start main menu
    menu.menu()

if __name__ == '__main__':
    main()
