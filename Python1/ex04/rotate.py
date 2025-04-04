import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from load_image import ft_load

def cut_square(image_array: np.ndarray) -> np.ndarray:
    """Cut the image into a square, by the center of the image;
    similar to the zoom function earlier but much simpler as we do not reshape the image;
    indeed we simply save the image from top (//2) to bottom and from left (//2) to right
    thus giving us a centered square"""
    height, width = image_array.shape[:2]
    square_size = min(height, width)
    
    top = (height - square_size) // 2
    left =  (width - square_size) // 2
    bottom = top + square_size
    right = left + square_size
    
    square_image = image_array[top:bottom, left:right]
    
    return square_image

def rotate_image(image_array: np.ndarray) -> np.ndarray:
    """Subject of our exercise, we will return the rotated image after loading it, cropping it and rotating clockwise"""
    height, width = image_array.shape[:2]
    rotated_image = np.zeros((width, height, image_array.shape[2]), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            rotated_image[j, height - i - 1] = image_array[i, j]
    return rotated_image

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
        image_array = ft_load(path)
    except FileNotFoundError as e:
        print(f"Error on Load of Image: {e}")
        return
    
    square_image = cut_square(image_array)
    rotated_image = rotate_image(square_image)
    display_axis(rotated_image)

if __name__ == "__main__":
    main()