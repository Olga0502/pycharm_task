from PIL import Image
import numpy as np

def get_brightness(pixels, pix_x, pix_y, size_moz):
    sum_color = np.sum(pixels[pix_x: pix_x + size_moz, pix_y: pix_y + size_moz])
    return int((sum_color / 3) // size_moz ** 2)


def set_color(pixels, pix_x, pix_y, size_moz, step):
    value_grey = get_brightness(pixels, pix_x, pix_y, size_moz)
    pixels[pix_x: pix_x + size_moz, pix_y: pix_y + size_moz] = int(value_grey // step) * step


def grey_img(pixels, gradation, size_moz):
    step = 255 // (gradation - 1)
    height = len(pixels)
    width = len(pixels[1])
    for pix_x in range(0, height, size_moz):
        for pix_y in range(0, width, size_moz):
            set_color(pixels, pix_x, pix_y, size_moz, step)
    return pixels


img = Image.open('img2.jpg')
arr_pixels = np.array(img)
size_moz = 10
gradation = 50
res = Image.fromarray(grey_img(arr_pixels, gradation, size_moz))
res.save('f2.jpg')