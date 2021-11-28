from PIL import Image
import numpy as np
import doctest


def get_brightness(pixels, pix_x, pix_y, size_moz):
    """
            Считает "шаг" серого цвета и возвращает среднюю яркость
            >>> get_brightness(np.array(Image.open('img2.jpg')), 5, 5, 10)
            18
            >>> get_brightness(np.array(Image.open("img2.jpg")), 15, 15, 5)
            19
    """
    sum_color = np.sum(pixels[pix_x: pix_x + size_moz, pix_y: pix_y + size_moz])
    return int((sum_color / 3) // size_moz ** 2)


def set_color(pixels, pix_x, pix_y, size_moz, step):
    """
    Закрашивает каждый пиксель в один цвет средней яркости
    """
    value_grey = get_brightness(pixels, pix_x, pix_y, size_moz)
    pixels[pix_x: pix_x + size_moz, pix_y: pix_y + size_moz] = int(value_grey // step) * step


def grey_img(pixels, gradation, size_moz):
    """"
    Возвращает итоговое изображение в серых оттенках
    """
    step = 255 // (gradation - 1)
    height = len(pixels)
    width = len(pixels[1])
    pix_x = 0
    while pix_x < height:
        pix_y = 0
        while pix_y < width:
            set_color(pixels, pix_x, pix_y, size_moz, step)
            pix_y = pix_y + size_moz
        pix_x = pix_x + size_moz
    return pixels


if __name__ == '__main__':
    doctest.testmod()


file_image = input("Введите имя входного файла")
img = Image.open(file_image)
arr_pixels = np.array(img)
size_moz = int(input("Введите размер желаемой мозайки"))
gradation = int(input("Введите количество градаций(число)"))
res_image = input("Введите имя файла для сохранения")
res = Image.fromarray(grey_img(arr_pixels, gradation, size_moz))
res.save(res_image)
