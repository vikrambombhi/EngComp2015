from Cimpl import *
import Cimpl
import sys
import glob
sys.setrecursionlimit(990000000)
list_of_image = glob.glob('Data Set/*.bmp')
list_of_image = [s.replace('Data Set\\', '') for s in list_of_image]
result = []
for image in list(list_of_image):
    path = 'Data Set/%s' % image
    img = Cimpl.load_image(path)

    def lower_brightness(img):

        average_brightness = 0
        min_brightness = 60

        for x, y, col in img:

            r, g, b = col

            brightness = (r+g+b) // 3

            average_brightness += brightness

        average_brightness //= (150*150)

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
        """(Cimpl.Image) -> (Int)

        Scans image for white pixel chunks. Returns the size of the largest chunk.
        """
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
        """(Cimpl.Image, Int, Int) -> (Int)

        Recursively determines the size of a chunk in pixels.
        """
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
        """
        (Cimpl.image)->(Cimple.image)
        Creates a more general picture by using the average color to
        all pixels in 3x3 grid
        >>> image = load_image(choose_file())
        >>> show(filter_resolution(image))
        """

        lastpixel = (0, 0)

        for x, y, col in img:
            (xL, yL) = lastpixel

            sum_color = 0

            if (x >= 10 and x <= 140) and (y >= 10 and x <= 140):
                #Inside border

                if (x >= (3 + xL)) or (y >= (3 + yL)):
                    #Is 1 box width away

                    for x2 in range(-1, 2):

                        for y2 in range(-1, 2):

                            color = get_color(img, (x + x2), (y + y2))
                            r, g, b = color

                            sum_color += ((r + g + b)//3) # will add either 0 or 255

                    if(sum_color >= 1275): # 5 or more pixels of out 9 are white, changes all 9 to white

                        for x2 in range(-1, 2):

                            for y2 in range(-1, 2):
                                new_color = create_color(255, 255, 255)
                                set_color(img, (x + x2), (y + y2), new_color)

                    else: # 5 or more pixels of out 9 are black, changes all 9 to black

                        for x2 in range(-1, 2):

                            for y2 in range(-1, 2):
                                new_color = create_color(0, 0, 0)
                                set_color(img, (x + x2), (y + y2), new_color)

                    lastpixel = (x, y)

        return img

    def final_check(img):

        image_value = scan(img)

        if 750 < image_value < 1300:
            return 'Pass'
        else:
            return 'Fail'

    lower_brightness(img)
    ans = final_check(img)
    result.append('%s = %s' % (image, ans))
print(result)
