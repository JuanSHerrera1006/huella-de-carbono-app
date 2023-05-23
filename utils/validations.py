def integer_input(msg, a, b):
    """Function to validate if a integer is within a range (a, b)
    
    Parameters
    ----------
        msg: str
            Message to show in the prompt 
        a: int
            Min range value
        b: int 
            Max range value

    Returns
    -------
        ans: int
            Return the validate user input
    """
    while True:
        try:
            value = int(input(msg))
            if value < a or value > b:
                raise ValueError("Has ingresado un valor no valido ")
            return value
        except ValueError as e:
            print(e)


def real_input(msg, a, b):
    """Function to validate if a real is within a range (a, b)
    
    Parameters
    ----------
        msg: str
            Message to show in the prompt 
        a: int
            Min range value
        b: int 
            Max range value

    Returns
    -------
        ans: float
            Return the validate user input
    """
    while True:
        try:
            value = float(input(msg))
            if value < a or value > b:
                raise ValueError("Has ingresado un valor no valido")
            return value
        except ValueError as e:
            print(e)
    
def char_input(msg, valid_options=["M", "F"]):
    """Function to validate if a value is on a list
    
    Parameters
    ----------
        msg: str
            Message to show in the prompt 
        valid_options: list[str]
            List the valid elements
            DEFAULT: ["M", "F"]

    Returns
    -------
        ans: str
            Return the validate user input
    """
    while True:
        try:
            value = input(msg).upper()
            if value in valid_options:
                return value
            raise ValueError("Has elegido una opcion no valida")
        except ValueError as e:
            print(e)

def numeric_input(msg):
    """Function to check if a value is numeric

    Parameters
    ----------
        msg: str
            Message to show in the prompt 

    Returns
    -------
        ans: str
            Return the validate user input
    """ 
    while True:
        try:
            value = input(msg)
            if value.isnumeric():
                return value
            raise ValueError("Has digitado un numero de identificacion no valido (solo numerico)")
        except ValueError as e:
            print(e)
