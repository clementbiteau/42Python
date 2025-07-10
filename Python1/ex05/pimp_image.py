import numpy as np
import array
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(array) -> array:
    """As explained in the main, we will invert the colors of the image thus inverting the colors code.
    If the shade scale is indeed 255, we will simply return the result array by 255 minus the current color seen at index."""
    res = array.copy()
    for i in range(len(res)):
        for j in range(len(res[i])):
            for k in range(3):
                res[i][j][k] = 255 - res[i][j][k]
    return res
                
def ft_red(array) -> array:
    res = array.copy()
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j][1] = res[i][j][1] * 0
            res[i][j][2] = res[i][j][2] * 0
    return res
    
def ft_green(array) -> array:
    res = array.copy()
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j][0] = res[i][j][0] - res[i][j][0]
            res[i][j][2] = res[i][j][2] - res[i][j][2]
    return res
    
def ft_blue(array) -> array:
    res = array.copy()
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j][0] = 0
            res[i][j][1] = 0
    return res

def ft_grey(array) -> array:
    res = array.copy().astype('uint32')
    for i in range(len(res)):
        for j in range(len(res[i])):
            grey = (res[i][j][0] + res[i][j][1] + res[i][j][2]) / 3
            res[i][j][0] = grey
            res[i][j][1] = grey
            res[i][j][2] = grey
    return res

def main():
    """pimp_image() is a simple implementation of colour tampering by inverting, nulling or adding texture of the three
    colours Red Green Blue -> RGB
    On the spectrum of colours, RGB is a 3-index array [0 = R][1 = G][2 = B] on 255 shade scale"""
    
    img = ft_load('./landscape.jpg')
    
    filters = [
        ('Figure VIII.1: Original', img),
        ('Figure VIII.2: Invert', ft_invert(img)),
        ('Figure VIII.3: Red', ft_red(img)),
        ('Figure VIII.4: Green', ft_green(img)),
        ('Figure VIII.5: Blue', ft_blue(img)),
        ('Figure VIII.6: Grey', ft_grey(img)),
        ('Figure VIII.7: Weird-1', ft_invert(ft_red(img))),
        ('Figure VIII.7: Weird-2', ft_invert(ft_blue(img))),
        ('Figure VIII.7: Weird-3', ft_invert(ft_green(img)))

    ]
    
    plt.figure(figsize=(15, 10))
    for i, (title, data) in enumerate(filters, 1):
        plt.subplot(4, 3, i)
        plt.imshow(data.astype('uint8'))
        plt.title(title)
        plt.axis('off')    

    plt.tight_layout()
    plt.savefig("pimped_landscape.png")
    plt.show()

if __name__ == "__main__":
    main()