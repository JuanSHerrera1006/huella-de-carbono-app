import database.database as database
import menu.menu as menu
import utils.images as images_functions

def main():
    conn = database.create_connection()
    database.create_tables(conn)
    a, b = images_functions.image2blob()
    file_name = 'cat' + a 
    img = images_functions.blob2image(b)
    images_functions.save_image(img, file_name)



if __name__ == '__main__':
    main()
