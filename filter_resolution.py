from Cimpl import *

def filter_resolution(img, res):
    lastpixel = (0, 0)    
    for x,y,col in img:
        xlast, ylast = lastpixel
        if (x >= (xlast + res) or y>= (ylast + res)):
            #if x >= last x + resolution or if y>= lasty + resolution
            #then average, else, do nothing
            rtot = 0
            gtot = 0
            btot = 0
            # these total values for their respective colours will help determine average brightness
            #reset these for every 3x3 grid
            for y2 in range(-1, 2):
                for x2 in range(-1, 2):
                    #loop through element (resXres square)
                    rtoadd, gtoadd, btoadd = img.get_color(x + x2, y + y2)
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
    #return modified img
    return img