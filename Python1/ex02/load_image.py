from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray: #(you can return to the desired format)
    """ft_load() a function to load an image and print its format and its pixels in RGB"""
    try:
        image = Image.open(path)
    except FileNotFoundError:
        print(f"File not Found: image has not been found at {path}")
        exit()
    except Exception as e:
        print("Error: image has not been opened successfully")
        exit()
    
    width, height = image.size
    mode = image.mode
    
    if mode == 'RGB':
        channels = 3
    elif mode == 'RGBA':
        channels = 4
    elif mode == 'L':
        channels = 1
    else:
        channels = None
        
    print(f"The shape of the image is : ({width},{height},{channels})")
    print(mode)
    
    image_rgb = image.convert('RGB')
    return np.array(image_rgb)