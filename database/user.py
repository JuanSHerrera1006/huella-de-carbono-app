import constants.constants as constants


def get_all_user(connection):
    """Get all the users registered in the database

    Parameters
    ----------
        connection: Connection
            The connection with the database

    Returns
    -------
        users: list[Any]
            List with the users registered in the database. Return an empty list if the query failed
    """
    users = [] 
    with connection:
        try:
            cur = connection.cursor()
            users = cur.execute(constants.GET_ALL_USERS).fetchall()
        except ValueError as e:
            print(e)
    return users

def get_user_by_id(connection, reference):
    """Get the user with the reference choosed

    Parameters
    ----------
        connection: Connection
            The connection with the database
        reference: str
            The user id to search in the database
        
    Returns
    -------
        user: list[Any]
            List with the user registered in the database. Return an empty list if the query failed
    """
    user = []
    with connection:
        try:
            cur = connection.cursor()
            user = cur.execute(constants.GET_USER_BY_ID, (reference, )).fetchall()
        except ValueError as e:
            print(e)
    return user


def add_user(connection, reference, name, gender,place_of_birth, place_of_residence):
    """Insert a new register in the table "user"

    Parameters
    ----------
        connection: Connection
            The connection with the database
        reference: str
            The ID of the user
        name:
            The user name to be register
        gender:
            The gender of the user
        place_of_birth:
            The user place of birth
        place_of_residence
            the actual residence place of the user

    Returns
    -------
        None
    """
    with connection:
        try:
            cur = connection.cursor()
            params = (reference, name, gender, place_of_birth, place_of_residence)
            cur.execute(constants.INSERT_USER, params)
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)
    
def del_user_by_id(connection, reference) -> None:
    """Delete a user with the reference choosed

    Parameters
    ----------
        connection : Connection
            The connection with the database
        reference : str
            The ID of the user
    
    Returns
    -------
        None
    """
    with connection:
        try:
            cur = connection.cursor()
            cur.execute(constants.DEL_USER_BY_ID, (reference, ))
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)

