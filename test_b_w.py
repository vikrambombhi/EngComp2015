from Cimpl import *
import sys
sys.setrecursionlimit(10000)

def black_and_white(img, threshold):
    """ (Cimpl.Image) -> None

    Convert the specified image to a black-and-white (two-tone) image.

    >>> image = load_image(choose_file())
    >>> black_and_white(image)
    >>> show(image)
    """

    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on whether
    # its brightness is in the lower or upper half of this range.

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    number = 0
    for x, y, col in img:
        red, green, blue = col

        brightness = (red + green + blue) // 3

        if brightness < threshold:
            set_color(img, x, y, black)
        else:     # brightness is between threshold and 255, inclusive
            set_color(img, x, y, white)
            number += 1
    print(number)


def scan(img):
    black_and_white(img, 70)
    lst = []

    for x, y, col in img:
        red, green, blue = col
        if (x > 10) and (x < 140) and (y > 10) and (y < 140):
            if red == 255:
                lst.append(sumplusplus(img, x, y))

    largest = 0
    for number in lst:
        if largest <= number:
            largest = number

    return largest

green_color = create_color(0, 255, 0)


def sumplusplus(img, x, y):
    col = get_color(img, x, y)
    r, g, b = col
    if r == 255:
        sump = 0
        set_color(img, x, y, green_color)
        sump += 1
        if x + 1 < 150:
            sump += sumplusplus(img, x + 1, y)
            if y + 1 < 150:
                sump += sumplusplus(img, x + 1, y + 1)
            if y - 1 > 0:
                sump += sumplusplus(img, x + 1, y - 1)
        if x - 1 > 0:
            sump += sumplusplus(img, x - 1, y)
            if y + 1 < 150:
                sump += sumplusplus(img, x - 1, y - 1)
            if y - 1 > 0:
                sump += sumplusplus(img, x - 1, y + 1)
        if y + 1 < 150:
            sump += sumplusplus(img, x, y + 1)
        if y - 1 > 0:
            sump += sumplusplus(img, x, y - 1)

        return sump
    else:
        return 0

image = load_image(choose_file())
black_and_white(image, 70)
print(scan(image))
show(image)
