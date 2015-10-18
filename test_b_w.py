from Cimpl import *

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

    for x, y, col in img:
        red, green, blue = col

        brightness = (red + green + blue) // 3

        if brightness < threshold:
            set_color(img, x, y, black)
        else:     # brightness is between threshold and 255, inclusive
            set_color(img, x, y, white)
            