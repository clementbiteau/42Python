from PIL import Image
import numpy as np

# We use NumPy (Numerical Python) for its advantages in handling efficiently data structures like lists.
# NumPy offers strong 1D, 2D and higher dimension mathematical movements whether they are linear or in matrixes.
# NumPy uses vectorization: it applies an action or a set of actions on the entire array, not as a loop, as a whole.
# NumPy has been made in C ==> Importance of Speed

def ft_load(path: str) -> np.ndarray: #(you can return to the desired format)
    """ft_load() a function to load an image and print its format and its pixels in RGB;
    -> We intake one parameter: the path to the image we want to load;
    -> We return an NumPy image for the sake of efficiency in memory and storage;"""
    try:
        image = Image.open(path)
    except FileNotFoundError:
        print(f"File not Found: image has not been found at {path}")
        exit()
    except Exception as e:
        print("Error: image has not been opened successfully")
        exit()
    
    width, height = image.size    
    image_rgb = image.convert('RGB')
    image_array = np.array(image_rgb)
      
    print(f"The shape of the image is : ({width},{height},{image_array.shape[2]})")
    print(image_array)
    
    return image_array