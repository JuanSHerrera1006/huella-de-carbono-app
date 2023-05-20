import os

def get_root_dir() -> str:
    """Get the root path project
    
    Returns
    -------
        root_dir: str
            Absolute path of the root path project
    """
    CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
    ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
    return ROOT_DIR
