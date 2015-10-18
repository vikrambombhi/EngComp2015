from Cimpl import *
import sys
sys.setrecursionlimit(990000000)

def lower_brightness(img):

    average_brightness = 0
    min_brightness = 60

    for x, y, col in img:

        r, g, b = col

        brightness = (r+g+b) / 3

        average_brightness += brightness

    average_brightness /= (150*150)

    if average_brightness >= min_brightness:

        for x, y, col in img:

            r, g, b = col

            new_col = create_color((r*(3/4)), (g*(3/4)), (b*(3/4)))
            set_color(img, x, y, new_col)

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


def scan(img):
    black_and_white(img, 75)
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

def filter_resolution(img):
    lastpixel = (0, 0)
    for x, y, col in img:
        (xL, yL) = lastpixel
        if (x >= 10 and x <= 140) and (y >= 10 and x <= 140):
            #Inside border
            if (x >= (3 + xL)) or (y >= (3 + yL)):
                #Is 1 box width away
                for x2, y2 in range(-1, 2):
                    color = get_color(img, (x + x2), (y + y2))
                    r, g, b = color
                    if ((r + g + b) // 3 >= 135):
                        set_color(img, (x + x2), (y + y2), create_color(255, 255, 255))
                    else:
                        set_color(img, (x + x2), (y + y2), create_color(0, 0, 0))
        lastpixel = (x, y)
    return img

def final_check(img):

    image_value = scan(img)

    if 750 < image_value:
        print("Object passes test")
    else:
        print("Object does not passes test")


image = load_image(choose_file())
lower_brightness(image)
final_check(image)