import constants.constants as constants


def get_all_records(connection):
    record = [] 
    with connection:
        try:
            cur = connection.cursor()
            record = cur.execute(constants.GET_ALL_RECORDS).fetchall()
            # Close cursor
            cur.close()
        except ValueError as e:
            print(e)
    return record



def get_record(connection, reference, id_food):
    """Get the feeding record with the user reference and id_food

    Parameters
    ----------
        connection : Connection
            The connection with the database
        reference : str
            The ID user 
        id_food : int
            The ID food
    
    Returns
    -------
        None
    """
    record = [] 
    with connection:
        try:
            cur = connection.cursor()
            params = (reference, id_food)
            record = cur.execute(constants.GET_RECORD, params).fetchall()
            # Close cursor
            cur.close()
        except ValueError as e:
            print(e)
    return record



def get_records_by_reference(connection, reference):
    """Get all records of a user

    Parameters
    ----------
        connection : Connection
            The connection with the database
        reference : str 
            The ID user

    Returns
    -------
        None
    """
    records = [] 
    with connection:
        try:
            cur = connection.cursor()
            records = cur.execute(constants.GET_RECORDS_BY_REFERENCE, (reference, )).fetchall()
            # Close cursor
            cur.close()
        except ValueError as e:
            print(e)
    return records

def add_record(connection, id_user, id_food, consumption_per_day):
    """Insert a new register in the table "record"

    Parameters
    ----------
        connection: Connection
            The connection with the database
        id_user : string
            The reference of the user
        id_food : int
            The ID to the food
        consumption_per_day : int
            The number of consumptions per day
    Returns
    -------
        None
    """
    with connection:
        try:
            cur = connection.cursor()
            params = (id_user, id_food, consumption_per_day)
            cur.execute(constants.INSERT_RECORD, params)
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)

def update_record(connection, id_user, id_food, consumption_per_day):
    """Update a record with the id_user and id_food

    Parameters
    ----------
        connection : Connection
            The connection with the database
        id_user : str
            The ID user
        id_food : int
            The ID food
        consumption_per_day : int
            The consumptions per day to selected food

    Returns
    -------
        None 
    """
    with connection:
        try:
            cur = connection.cursor()
            params = (consumption_per_day, id_user, id_food)
            cur.execute(constants.UPDATE_RECORD_CONSUMPTION, params)
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)

def del_record(connection, reference, id_food):
    """Delete a record with the id_user and id_food

    Parameters
    ----------
        connection : Connection
            The connection with the database
        reference : str
            The ID user
        id_food : int
            The ID food

    Returns
    -------
        None 
    """
    with connection:
        try:
            cur = connection.cursor()
            params = (reference, id_food)
            cur.execute(constants.DEL_RECORD, params)
            # Save the changes in the database
            connection.commit()
            # Close the cursor
            cur.close()
        except ValueError as e:
            print(e)

def get_highest_co2_emmission_by_gender(connection):
    """Get the highest co2 emmission by gender

    Parameters
    ----------
        connection : Connection
            The connection with the database

    Returns
    -------
        records : list[Any]
            
    """
    records = [] 
    with connection:
        try:
            cur = connection.cursor()
            records = cur.execute(constants.GET_HIGHEST_CO2_EMMISSION_BY_GENDER).fetchall()
            # Close cursor
            cur.close()
        except ValueError as e:
            print(e)
    return records

