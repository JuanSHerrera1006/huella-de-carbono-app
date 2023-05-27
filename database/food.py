import constants.constants as constants

def get_all_foods(connection):
    """Get all the foods registered in the database

    Parameters
    ----------
        connection: Connection
            The connection with the database

    Returns
    -------
        foods: list[Any]
            List with the foods registered in the database. Return an empty list if the query failed
    """
    foods = [] 
    with connection:
        try:
            cur = connection.cursor()
            foods = cur.execute(constants.GET_ALL_FOODS).fetchall()
        except ValueError as e:
            print(e)
    return foods

def get_img_food_by_id(connection, id_food, only_meta_data=True):
    """Get all the foods registered in the database

    Parameters
    ----------
        connection: Connection
            The connection with the database

    Returns
    -------
        foods: list[Any]
            List with the foods registered in the database. Return an empty list if the query failed
    """
    image = [] 
    with connection:
        try:
            cur = connection.cursor()
            if only_meta_data:
                image = cur.execute(constants.GET_IMAGE_NAME_BY_ID, (id_food, )).fetchall()
            else:
                image = cur.execute(constants.GET_IMAGE_BY_ID, (id_food, )).fetchall()
        except ValueError as e:
            print(e)
    return image

def update_img_food_by_id(connection, id_food, image_bytes, img_name, ext):
    """Update the food image by id

    Parameters
    ----------
        connection : Connection
            The connection with the database
        id_food : int
            The ID of the food
        image_bytes : bytes
            The new image in bytes to update in the database
        img_name : str
            The new image name
        ext : str
            The extension of the image
    
    Returns
    -------
        None
    """
    with connection:
        try:
            cur = connection.cursor()
            params = (image_bytes, img_name, ext, id_food)
            cur.execute(constants.UPDATE_IMAGE_BY_FOOD_ID, params)
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)

def update_food_by_id(connection, field, value, id_food):
    """Update a food field with the id choosed

    Parameters
    ----------
        connection : Connection
            The connection with the database
        field : str
            The field that will be change
        value: Any
            The new value to update in the database
        food_id : str
            The ID of the food

    Returns
    -------
        None
    """
    with connection:
        try:
            cur = connection.cursor()
            params = (value, id_food)

            if constants.FIELDS_FOOD_TABLE["name"] == field:
                cur.execute(constants.UPDATE_FOOD_NAME_BY_ID, params) 

            elif constants.FIELDS_FOOD_TABLE["co2_emmission"] == field: 
                cur.execute(constants.UPDATE_FOOD_CO2_EMMISSION_BY_ID, params) 

            else:
                raise ValueError("No se ha ingresado un campo valido")

            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)



def add_food(connection, name, co2_emmission):
    """Insert a new register in the table "food"

    Parameters
    ----------
        connection: Connection
            The connection with the database
        name: str
            The food name to be register
        co2_emmission: float
            The co2 emmision per kg

    Returns
    -------
        id_food: int | None
            Return the registered food id
    """
    with connection:
        id_food = -1
        try:
            cur = connection.cursor()
            params = (name, co2_emmission)
            cur.execute(constants.INSERT_FOOD, params)
            # Save the changes in the database
            connection.commit()
            # Get the id 
            id_food = cur.lastrowid
            # Close the cursor
            cur.close()
            return id_food
        except ValueError as e:
            print(e)

def add_food_img(connection, id_food, image, name, format_img):
    """Insert a new register in the table "food"

    Parameters
    ----------
        connection: Connection
            The connection with the database
        id_food : int
            The ID food to register the image
        image : bytes
            The image type bytes
        name: str
            The image name that it will be saving
        format_img: str
            The image format (.jpg, .jpeg, .png)
    Returns
    -------
        None
    """
    with connection:
        try:
            cur = connection.cursor()
            params = (id_food, image, name, format_img)
            cur.execute(constants.INSERT_FOOD_IMG, params)
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)

def del_food_by_id(connection, id_food):
    """Delete a food with the id_food choosed

    Parameters
    ----------
        connection : Connection
            The connection with the database
        id_food : str
            The ID of the food
    
    Returns
    -------
        None
    """
    with connection:
        try:
            cur = connection.cursor()
            cur.execute(constants.DEL_FOOD_BY_ID, (id_food, ))
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)

