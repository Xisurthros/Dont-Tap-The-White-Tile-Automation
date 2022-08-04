from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:
    # Finds loction on screen and checks for color value
    if pyautogui.pixel(1300, 400)[0] == 0:
        click(1300, 400)
    if pyautogui.pixel(1400, 400)[0] == 0:
        click(1400, 400)
    if pyautogui.pixel(1500, 400)[0] == 0:
        click(1500, 400)
    if pyautogui.pixel(1600, 400)[0] == 0:
        click(1600, 400)
