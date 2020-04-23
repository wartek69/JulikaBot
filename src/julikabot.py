import os
import time
import logging
import win32api, win32con
from helpers.mouse_helper import MouseHelper
import helpers.static_coordinates as sc
import helpers.keyboard_helper as keyboard
from helpers.image_helper import ImageHelper

x_pad = 319
y_pad = 154
game_width = 1281
game_height = 721

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')


class JulikaBot:
    def __init__(self):
        self.mouse_helper = MouseHelper(x_pad, y_pad)
        self.image_helper = ImageHelper(x_pad, y_pad, game_width, game_height)
    
    def find_coop_intermediate(self):
        logging.info('Finding a game...')
        self.mouse_helper.move_click_left_mouse(sc.PLAY_BUTTON)
        time.sleep(.5)
        logging.info('Clicked play button on coords {}'.format(sc.PLAY_BUTTON))
        self.mouse_helper.move_click_left_mouse(sc.COOP_BUTTON)
        time.sleep(.5)
        self.mouse_helper.move_click_left_mouse(sc.INTERMEDIATE_DIFFICULTY)
        time.sleep(.5)
        self.mouse_helper.move_click_left_mouse(sc.CONFIRM_BUTTON)
        time.sleep(3)
        #TODO Ensure that we can click the button, if that's done the sleep can be changed with a while loop
        self.mouse_helper.move_click_left_mouse(sc.CONFIRM_BUTTON)
        self.__go_in_loading_screen()
        logging.info('Done finding a game!')

    def select_soraka(self):
        logging.info('Selecting soraka...')
        self.mouse_helper.move_click_left_mouse(sc.CHAMP_SELECT_SEARCH)
        time.sleep(.5)
        keyboard.typer('soraka')
        self.mouse_helper.move_click_left_mouse(sc.CHAMP_SELECT_FIRST_CHAMP)
        time.sleep(.5)
        self.mouse_helper.move_click_left_mouse(sc.CHAMP_SELECT_LOCKIN)
    
    def prepare_for_game(self):
        self.__wait_for_ingame()
        self.__buy_items()
    '''
    Looks for a pixel that is in the timer of the loading screen
    '''
    def __go_in_loading_screen(self):
        pixel_color = (0, 0, 0)
        while pixel_color != (240, 230, 210):
            time.sleep(1)
            pixel_color = self.image_helper.screen_grab_game_window().getpixel(sc.CHAMP_SELECT_LOADING_SCREEN_TIMER)
            logging.debug('Pixel value is {}'.format(pixel_color))
            logging.info('Waiting for a game...')
            self.mouse_helper.move_click_left_mouse(sc.ACCEPT_MATCH_BUTTON)
    '''
    checks pixels of jungle on the minimap
    '''
    def __wait_for_ingame(self):
        mean_pixel_value = -1
        while mean_pixel_value != 2667:
            mean_pixel_value = self.image_helper.get_mean_pixel_value(
                sc.MINIMAP_JGL_RED_BUFF_UPPER_LEFT[0], 
                sc.MINIMAP_JGL_RED_BUFF_UPPER_LEFT[1], 
                sc.MINIMAP_JGL_RED_BUFF_LOWER_RIGHT[0], 
                sc.MINIMAP_JGL_RED_BUFF_LOWER_RIGHT[1])

            time.sleep(1)
            logging.debug('Waiting to go in game, mean pixel value: {}'.format(mean_pixel_value))
            if mean_pixel_value == 2198:
                logging.info('In loading screen...')
        logging.info('Game started!')

    def __toggle_shop(self):
        pass

    def __buy_items(self):
        self.__toggle_shop()
        pass






if __name__ == '__main__':
    mouse_helper = MouseHelper(x_pad, y_pad)
    julika_bot = JulikaBot()
    #julika_bot.find_coop_intermediate()
    julika_bot.select_soraka()
    while True:
        mouse_helper.get_coords()
        time.sleep(0.5)