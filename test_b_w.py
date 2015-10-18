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
        
        if red == 255:
            lst.append(3)
    
    largest = 0
    for number in lst:
        if largest <= number:
            largest = number
            
    return largest
            

def sumplusplus(img, x, y, col):

    green = (0, 255, 0)
    r, g, b = col
    if r == 255:
        sump = 0
        set_color(img, x, y, green)
        sump += 1
        sump += sumplusplus(img, x, y+1, col)
        sump += sumplusplus(img, x+1, y+1, col)
        sump += sumplusplus(img, x+1, y, col)
        sump += sumplusplus(img, x+1, y-1, col)
        sump += sumplusplus(img, x, y-1, col)
        sump += sumplusplus(img, x-1, y-1, col)
        sump += sumplusplus(img, x-1, y, col)
        sump += sumplusplus(img, x-1, y+1, col)
    else:
        return 0
