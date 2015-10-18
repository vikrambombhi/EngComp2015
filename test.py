__author__ = 'Tuanhao'

from Cimpl import *

def test_color(img):

    for x, y, col in img:

        r, g, b = col

        new_col = get_color(img, x, y)

    return new_col


