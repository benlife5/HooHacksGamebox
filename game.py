"""
Boardgame with minigames! (needs a better title)
Ben Life & Oliver Song
HooHacks 2021
Built on PyGame and Gamebox
Gamebox was built by Luther Tychonievich (tychonievich@virginia.edu)
"""

import pygame
import gamebox
camera = gamebox.Camera(1000,700)
miniGames = ["Matching Pairs"]
miniGame = None
gamePaused = True
currentIndex = 0

MPObjects = []

board_space_coords = []
for i in range(1, 13):
    board_space_coords.append((1, i))
for i in range(2, 5):
    board_space_coords.append((i, 12))
for i in range(12, 5, -1):
    board_space_coords.append((5, i))
board_space_coords.append((4, 6))
for i in range(6, 0, -1):
    board_space_coords.append((3, i))
for i in range(3, 8):
    board_space_coords.append((i, 1))
for i in range(1, 13):
    board_space_coords.append((7, i))
board_space_coords.append((8, 12))
board_space_coords.append((9, 12))
for i in range(12, 6, -1):
    board_space_coords.append((10, i))
board_space_coords.append((11, 7))
board_space_coords.append((12, 7))
for i in range(7, 2, -1):
    board_space_coords.append((13, i))
board_space_coords.append((14, 3))
for i in range(3, 13):
    board_space_coords.append((15, i))
board_space_coords.append((16, 12))
board_space_coords.append((17, 12))
for i in range(12, 0, -1):
    board_space_coords.append((18, i))
for i in range(18, 10, -1):
    board_space_coords.append((i, 1))


def displayStartScreen():
    camera.clear("white")
    camera.draw("Project Name!", 64, "black", 500, 100)
    camera.draw("Press Enter to Begin", 48, "black", 500, 150)


def drawMainBoard():
    for coord in board_space_coords:
        outer_box = gamebox.from_color(coord[0] * 50, coord[1] * 50, "black", 50, 50)
        inner_box = gamebox.from_color(coord[0] * 50 + 1, coord[1] * 50 + 1, "white", 46, 46)
        camera.draw(outer_box)
        camera.draw(inner_box)

def tick(keys):
    global gamePaused, miniGame, currentIndex

    if gamePaused:
        displayStartScreen()
        if pygame.K_RETURN in keys:
            gamePaused = False
            keys.clear()
    else:
        if miniGame is None:  # main game active
            camera.clear('grey')
            drawMainBoard()

            currentX = board_space_coords[currentIndex][0]
            currentY = board_space_coords[currentIndex][1]

            camera.draw(gamebox.from_image(50, 50, "green_star.png"))
            camera.draw(gamebox.from_image(11 * 50, 50, "gold_star.png"))
            camera.draw(gamebox.from_image(currentX * 50, currentY * 50, "red_circle.png"))

            if pygame.K_RETURN in keys:
                miniGame = ""
                keys.clear()

            if camera.mouseclick:
                currentIndex += 1
                if currentIndex >= len(board_space_coords):
                    print("Game Won!")
                    currentIndex = 0
                    gamePaused = True
        if miniGame == "":  # minigame 1
            camera.clear('white')
            if pygame.K_RETURN in keys:
                miniGame = None
                keys.clear()



    camera.display()


ticks = 30
gamebox.timer_loop(ticks, tick)