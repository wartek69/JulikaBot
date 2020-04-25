from abc import ABC, abstractmethod
from helpers.keyboard import keyboard_helper as keyboard
import time


class AbstractBot(ABC):
    @abstractmethod
    def __init__(self, mouse_helper):
        self.mouse_helper = mouse_helper

    @abstractmethod
    def buy_start_items(self):
        pass

    @abstractmethod
    def select_champion(self):
        pass

    @abstractmethod
    def act(self):
        pass

    def _focus_bot_ally(self):
        keyboard.pressAndHold_ingame('F2')
        time.sleep(.1)

    def _release_focus_bot_ally(self):
        keyboard.release_ingame('F2')
        time.sleep(.1)

    def _upgrade_spell(self, spell_number: int):
        spells = 'qwer'
        if spell_number > 3:
            spell_number = 3
        keyboard.pressHoldRelease_ingame('ctrl', spells[spell_number])
        time.sleep(.5)

    def _cast_spell(self, spell_number: int):
        spells = 'qwer'
        if spell_number > 3:
            spell_number = 3
        keyboard.press_ingame(spells[spell_number])

    def _toggle_shop(self):
        keyboard.press_ingame('p')
        time.sleep(1)


