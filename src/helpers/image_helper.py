from PIL import ImageGrab, ImageOps
import numpy as np
import logging 
class ImageHelper:

    def __init__(self, x_pad, y_pad, game_heigth, game_width):
        self._x_pad = x_pad
        self._y_pad = y_pad
        self._game_heigth = game_heigth
        self._game_width = game_width
        pass

    def screen_grab_game_window(self):
        self.__screen_grab(1, 1, self._game_width, self._game_heigth)
        #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    
    def __screen_grab(self, lux, luy, rlx, rly):
        bbox = (self._x_pad + lux, self._y_pad + luy, self._x_pad + rlx, self._y_pad + rly)
        im = ImageGrab.grab(bbox)
        return im
    '''
    Takes pixels bounded by a bounding box, transforms the rgb to grayscale and calculates the sum of the grey values
    Naive technique for detecting features
    :param int lux: leftupper x
    :param int luy: leftupper y
    :param int rlx: rightlower x
    :param int rly: rightlower y
    '''
    def get_mean_pixel_value(self, lux: int, luy: int, rlx: int, rly: int):
        im = ImageOps.grayscale(self.__screen_grab(lux, luy, rlx, rly))
        a = np.array(im.getcolors())
        a = a.sum()
        logging.debug('pixel sum: {}'.format(a))
        return a
