import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from load_image import ft_load

def zoom_image(image_array: np.ndarray, zooming: float) -> np.ndarray:
    if zooming < 1:
        print("Error: zoom must be greater than 1")
        return image_array
    
    # We use the shap[:2] because we want to exclude the third factor that will be the channel (L1, RGB3, RGBA4)
    # We use the syntax / because the height and zoom factor can be float -> we will shape it to integers
    height, width = image_array.shape[:2]
    new_height = int(height /zooming)
    new_width = int(width / zooming)
    
    # We use the syntax // to round down to the previous number (being an int) even if floats and ints are being vs
    top = (height - new_height) // 2
    left = (width - new_width) // 2
    bottom = (top + new_height)
    right = (left + new_width)
    
    # We use the Image.LANCZOS, an algorythm that exists to efficiently resize an image without losing too much
    # of its former quality. It is called, in the PIL lib : Lancsoz Resampling Filter
    cropped = image_array[top:bottom, left:right]
    zoomed = Image.fromarray(cropped).resize((width, height), Image.LANCZOS)
    print(f"New shape after slicing: ({new_width}, {new_height}, {image_array.shape[2]}) or ({new_width}, {new_height})")
    print(cropped)
    
    return zoomed

def display_axis(image_array: np.ndarray):
    """Required funtion to display the X and Y axes of the picutre that will be submitted to our zooming"""
    plt.imshow(image_array)
    plt.xlabel("X axis (Pixels)")
    plt.ylabel("Y axis (Pixels)")
    plt.title("Your Zoomed Picture")
    plt.colorbar(label = "Pixel Intensity")
    plt.show()

def main():
    """Main() will load an image from path + zoom it + show it zoomed with axis"""
    try:
        path = "animal.jpeg"
        zoom_factor = 2
        image_array = ft_load(path)
    except FileNotFoundError as e:
        print(f"Error on Load of Image: {e}")
        return
    
    zoomed_image = zoom_image(image_array, zoom_factor)
    display_axis(zoomed_image)

if __name__ == "__main__":
    main()