from tkinter.filedialog import askopenfilename
from utils.path import get_root_dir
from PIL import Image 
import matplotlib.pyplot as plt
import matplotlib.image as matplotlib_image
import constants.constants as constants
import os
import io

def image2blob():
    """Ask to file explorer and get the bytes of the selected image
    
    Returns
    -------
        ext: str
            The imagen extension (.jpg, .png, .jpeg)
        image_bytes:
            The image in bytes
    """
    img_path = ""
    # Ask to the file explorer
    while True:
        img_path = askopenfilename(filetypes=constants.IMAGES_FILETYPES)
        if img_path != "":
            break
        
        print("Debes de seleccionar un archivo de imagen tipo (.jpg, .png, .jpeg)")
        input("Presiona cualquier tecla para continuar...")
        print("")

    image = Image.open(img_path)
    img_format = image.format or 'JPEG'
    # Get the extension of the image
    _, ext = os.path.splitext(img_path)
    # Create the stream to save the image bytes
    stream = io.BytesIO()
    image.save(stream, img_format)
    image_bytes = stream.getvalue()
    return ext, image_bytes

def blob2image(image_bytes):
    """Convert the bytes of a image to class PIL.Image.Image

    Parameters
    ----------
        image_bytes: Bytes
            The bytes of the image

    Returns
    -------
        image: Image
            The image type PIL.Image.ImageDB Browser for SQLite
    """
    stream = io.BytesIO(image_bytes)
    return Image.open(stream)

def save_image(img, image_name):
    """Save the image in the path "ROOT_DIR\\assets\\image\\{image_name}.{ext}" of the project

    Parameters
    ----------
        img: Image
            The image type PIL.Image.Image
        image_name: str
            The name of the image. The name should have the extension on the finish.

    Returns
    -------
        None
    """
    ROOT_DIR = get_root_dir()
    DEST_PATH = ".\\assets\\images\\" + image_name
    IMG_PATH = os.path.abspath(os.path.join(ROOT_DIR, DEST_PATH))
    img.save(IMG_PATH)

def show_image(image_name):
    """Show the image and its name 

    Parameters
    ----------
        image_name: str
            The name of the image. The name should have the extension on the finish.

    Returns
    -------
        None
    """
    ROOT_DIR = get_root_dir()
    DEST_PATH = ".\\assets\\images\\" + image_name
    IMG_PATH = os.path.abspath(os.path.join(ROOT_DIR, DEST_PATH))
    # Plot image
    fig = matplotlib_image.imread(IMG_PATH)
    plt.imshow(fig)
    plt.axis('off')
    plt.title(image_name)
    plt.show()
