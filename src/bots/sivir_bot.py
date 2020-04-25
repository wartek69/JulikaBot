from .abstract_bot import AbstractBot
import logging
import time
from helpers import static_coordinates as sc
import helpers.keyboard.keyboard_helper as keyboard

'''
sivir bot, atm just follows ally and auto attacks everything in the neighbourhood
'''

class SivirBot(AbstractBot):
    def __init__(self, mouse_helper):
        super().__init__(mouse_helper)
        self.game_start_timestamp = 0

    def act(self):
        # Upgrade spells, if you cannot upgrade a spell this won't do anything
        self._upgrade_spell(3)
        self._upgrade_spell(1)
        self._upgrade_spell(0)
        self._upgrade_spell(2)

        self._focus_bot_ally()
        self.mouse_helper.move_click_right_mouse(sc.CAMERA_LOCK_CHAMP)
        time.sleep(.5)
        if time.time() - self.game_start_timestamp > 120:
            pass

        self._cast_spell(3)
        self._release_focus_bot_ally()
        time.sleep(1)
        logging.info('action done')
    
    def buy_start_items(self):
        self.game_start_timestamp = time.time()
        time.sleep(2)
        self._toggle_shop()
        self.mouse_helper.move_click_right_mouse(sc.SHOP_START_ITEM_1)
        time.sleep(.5)
        self.mouse_helper.move_click_right_mouse(sc.SHOP_START_ITEM_2)
        time.sleep(.5)
        self.mouse_helper.move_click_right_mouse(sc.SHOP_START_ITEM_3)
        time.sleep(.5)
        self._toggle_shop()
        logging.info('Bought start items')

    def select_champion(self):
        logging.info('Selecting sivir...')
        self.mouse_helper.move_click_left_mouse(sc.CHAMP_SELECT_SEARCH)
        time.sleep(.5)
        keyboard.typer('sivir')
        self.mouse_helper.move_click_left_mouse(sc.CHAMP_SELECT_FIRST_CHAMP)
        time.sleep(.5)
        self.mouse_helper.move_click_left_mouse(sc.CHAMP_SELECT_LOCKIN)