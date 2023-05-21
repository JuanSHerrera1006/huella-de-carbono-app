from utils.path import get_root_dir
import os
import csv

def create_csv(filename: str, header: tuple, data: tuple) -> None:
    """Create csv document in the path: "ROOT_DIR\\csv_data\\filename.csv" of the project

    Parameters
    ----------
        filename: str
            The name of the file to save in the path. The name should have ".csv" in the finish
        header: tuple
            The header of the csv file
        data: tuple
            The data of the csv file

    Returns
    -------
        None 
    """
    ROOT_DIR = get_root_dir()
    DEST_DIR = ".\\csv_data\\" + filename
    FILE_PATH = os.path.abspath(os.path.join(ROOT_DIR, DEST_DIR))

    with open(FILE_PATH, 'w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        # Write header of CSV
        writer.writerow(header)
        # Write the data
        writer.writerows(data)

