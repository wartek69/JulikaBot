import os
import time
import logging
import win32api, win32con
from helpers.mouse_helper import MouseHelper
import helpers.static_coordinates as sc
import helpers.keyboard.keyboard_helper as keyboard
from helpers.image_helper import ImageHelper
import helpers.process_helper as process_helper
from bots.soraka_bot import SorakaBot
from bots.sivir_bot import SivirBot

x_pad = 319
y_pad = 154
game_width = 1281
game_height = 721

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')


class JulikaBotEngine:
    def __init__(self, bot, mouse_helper):
        self.mouse_helper = mouse_helper
        self.image_helper = ImageHelper(x_pad, y_pad, game_width, game_height)
        self.bot = bot
    
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
    
    def prepare_for_game(self):
        self.bot.select_champion()
        self.__wait_for_ingame()
        #make sure the client is focussed
        self.mouse_helper.move_click_right_mouse(sc.CAMERA_LOCK_CHAMP)
        self.bot.buy_start_items()
        
    def __in_game(self):
        return process_helper.checkIfProcessRunning('League of Legends')

    def play_game(self):
        logging.info('playing game...')
        while self.__in_game():
            self.bot.act()
        logging.info('Game done!')

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
        while mean_pixel_value != 2289:
            mean_pixel_value = self.image_helper.get_mean_pixel_value(
                sc.MINIMAP_JGL_RED_BUFF_UPPER_LEFT[0], 
                sc.MINIMAP_JGL_RED_BUFF_UPPER_LEFT[1], 
                sc.MINIMAP_JGL_RED_BUFF_LOWER_RIGHT[0], 
                sc.MINIMAP_JGL_RED_BUFF_LOWER_RIGHT[1])

            time.sleep(1)
            logging.debug('Waiting to go in game, mean pixel value: {}'.format(mean_pixel_value))
            if mean_pixel_value == 1246:
                logging.info('In loading screen...')
        logging.info('Game started!')





if __name__ == '__main__':
    mouse_helper = MouseHelper(x_pad, y_pad)
    sorakaBot = SivirBot(mouse_helper)
    julika_bot = JulikaBotEngine(sorakaBot, mouse_helper)
    #julika_bot.find_coop_intermediate()
    julika_bot.prepare_for_game()
    julika_bot.play_game()
    while True:
        mouse_helper.get_coords()
        time.sleep(0.5)