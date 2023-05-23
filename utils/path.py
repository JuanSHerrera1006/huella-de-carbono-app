import os

def get_root_dir():
    """Get the root path project
    
    Returns
    -------
        root_dir: str
            Absolute path of the root path project
    """
    CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
    ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
    return ROOT_DIR

def path_exists(path):
    """Check if the path exists

    Parameters
    ----------
        path: str
            The path that will be verify

    Returns
    -------
        ans: bool
            The results if the path exists
    """
    ROOT_DIR = get_root_dir()
    DEST_DIR = os.path.abspath(os.path.join(ROOT_DIR, path))
    return os.path.exists(DEST_DIR)

def remove_file(path):
    """Remove a file of a path

    Parameters
    ----------
        path: str
            Path of the file to delete

    Returns
    -------
        None
    """
    ROOT_DIR = get_root_dir()
    DEST_DIR = os.path.abspath(os.path.join(ROOT_DIR, path))
    return os.remove(DEST_DIR)
