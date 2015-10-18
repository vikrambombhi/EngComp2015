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

    return img

def filter_resolution(img):
    lastpixel = (0, 0)
    for x, y, col in img:
        xlast, ylast = lastpixel
        if (x >= (xlast + 3) or y>= (ylast + 3)):
            #if x >= last x + resolution or if y>= lasty + resolution
            #then average, else, do nothing
            rtot = 0
            gtot = 0
            btot = 0
            # these total values for their respective colours will help determine average brightness
            #reset these for every 3x3 grid
            for y2 in range(-1, 1):
                for x2 in range(-1, 1):
                    #loop through element (resXres square)

                    newx = x + x2
                    newy = y + y2

                    new_col = get_color(img, newx, newy)

                    rtoadd, gtoadd, btoadd = new_col
                    rtot += rtoadd
                    gtot += gtoadd
                    btot += btoadd
                    # update the totals
                    if (rtot + gtot + btot / 3 >= (255 * (5.0 * 9.0))):
                       #set_color(img, x, y, new_color(255, 255, 255) for every pixel in range since its
                        set_color(img, x + x2, y + y2, new_color(255, 255, 255))
                    else:
                        set_color(img, x + x2, y + y2, new_color(0, 0, 0))
                    # done filter
    lastpixel = (x, y)
    #return modified img
    return img
#-----------------------------------------------------------

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

accepted_value = 900

def final_check(img):

    complete_peice = False

    image_value = scan(img)

    if image_value >= accepted_value:
        complete_peice = True

image = load_image(choose_file())
black_and_white(image, 70)
print(scan(image))
show(image)
