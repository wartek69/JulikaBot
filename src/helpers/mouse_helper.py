import os
import time
import logging
import win32api, win32con

class MouseHelper:
    def __init__(self, x_pad, y_pad):
        self.x_pad = x_pad
        self.y_pad = y_pad

    def left_click(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def right_click(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

    def move_mouse(self, coord):
        win32api.SetCursorPos((self.x_pad + coord[0], self.y_pad + coord[1]))
    
    def move_click_left_mouse(self, coord):
        self.move_mouse(coord)
        time.sleep(.1)
        self.left_click()
        
    def move_click_right_mouse(self, coord):
        self.move_mouse(coord)
        time.sleep(.1)
        self.right_click()

    def get_coords(self):
        x, y = win32api.GetCursorPos()
        x = x - self.x_pad
        y = y - self.y_pad
        logging.info('x: {} y: {}'.format(x, y))
