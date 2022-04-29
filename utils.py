from PIL import Image
from numpy import asarray
import base64
import io

def loadImgToArray(path: str):
    return imgToArray(loadImage(path))

def loadImage(path: str):
    return Image.open(path)
    
def imgToArray(img): 
    return asarray(img)

def base64ToArray(data):
    decoded = base64.b64decode(data)
    image = Image.open(io.BytesIO(decoded))
    return asarray(image)

def read_file(filename):
    print(filename)
    with open(filename, 'r') as infile:
        text = infile.read()
    return text