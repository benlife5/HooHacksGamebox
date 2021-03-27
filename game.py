"""
Boardgame with minigames! (needs a better title)
Ben Life & Oliver Song
HooHacks 2021
Built on PyGame and Gamebox
Gamebox was built by Luther Tychonievich (tychonievich@virginia.edu)
"""

import pygame
import gamebox
camera = gamebox.Camera(800,600)


def tick(keys):
    camera.clear('white')
    camera.display()

ticks = 30
gamebox.timer_loop(ticks, tick)