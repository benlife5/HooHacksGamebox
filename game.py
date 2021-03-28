"""
Boardgame with minigames! (needs a better title)
Ben Life & Oliver Song
HooHacks 2021
Built on PyGame and Gamebox
Gamebox was built by Luther Tychonievich (tychonievich@virginia.edu)
"""

import pygame
import gamebox
import random
camera = gamebox.Camera(1000,700)
miniGames = ["ClickingRainbow", "Maze"]
miniGame = None
gamePaused = True
currentIndex = 0
num_of_rolls = 0
rollingActive = False
final_roll = None

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

# Clicking rainbow minigame
CRDirections = gamebox.from_text(500, 50, 'Touch the boxes in the order of rainbow colors!', 40, "Black")
CRObjects = {1: [gamebox.from_color(random.randint(50, 500), random.randint(50, 300), "red", 30, 30), 1, False],
             2: [gamebox.from_color(random.randint(500, 950), random.randint(300, 650), "orange", 30, 30), 2, False],
             3: [gamebox.from_color(random.randint(50, 500), random.randint(50, 300), "yellow", 30, 30), 3, False],
             4: [gamebox.from_color(random.randint(500, 950), random.randint(300, 650), "green", 30, 30), 4, False],
             5: [gamebox.from_color(random.randint(50, 500), random.randint(50, 300), "blue", 30, 30), 5, False],
             6: [gamebox.from_color(random.randint(500, 950), random.randint(300, 650), "purple", 30, 30), 6, False],
             7: [gamebox.from_color(100, 100, "black", 30, 30), "black", False]}
mouse1 = 0

# Maze Minigame
MazeObjects = [gamebox.from_color(0, 350, "red", 20, 700),
               gamebox.from_color(60, 200, "red", 100, 20),
               gamebox.from_color(200, 175, "red", 20, 350),
               gamebox.from_color(200, 350, "red", 230, 20),
               gamebox.from_color(97, 500, "red", 20, 300),
               gamebox.from_color(200, 600, "red", 20, 300),
               gamebox.from_color(303, 500, "red", 20, 300),
               gamebox.from_color(400, 525, "red", 20, 350),
               gamebox.from_color(500, 100, "red", 20, 350),
               gamebox.from_color(310, 100, "red", 200, 20),
               gamebox.from_color(310, 200, "red", 20, 190),
               gamebox.from_color(500, 500, "red", 20, 300),
               gamebox.from_color(600, 175, "red", 20, 350),
               gamebox.from_color(600, 360, "red", 200, 20),
               gamebox.from_color(700, 500, "red", 20, 300),
               gamebox.from_color(705, 250, "red", 200, 20),
               gamebox.from_color(850, 150, "red", 350, 20),
               gamebox.from_color(800, 525, "red", 20, 350),
               gamebox.from_color(900, 525, "red", 20, 350),
               gamebox.from_color(1000, 350, "red", 20, 700)]
mazePlayer = gamebox.from_color(50, 100, "black", 30, 30)
destination = gamebox.from_color(900, 50, "yellow", 30, 30)

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
    global gamePaused, miniGame, currentIndex, num_of_rolls, rollingActive, final_roll, mouse1

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

            camera.draw(gamebox.from_color(12 * 50 + 25, 9 * 50 + 25, "white", 100, 100))

            if final_roll is not None:
                camera.draw(str(final_roll), 48, "black", 12 * 50 + 25, 9 * 50 + 25)
                camera.draw("Click to Play a Minigame", 24, "black", 12 * 50 + 25, 11 * 50)
            else:
                camera.draw("Click to Roll", 24, "black", 12 * 50 + 25, 11 * 50)

            if rollingActive:
                if num_of_rolls < 60:
                    temp_roll = random.randint(1, 6)
                    camera.draw(str(temp_roll), 48, "black", 12 * 50 + 25, 9 * 50 + 25)
                    num_of_rolls += 1
                else:
                    final_roll = random.randint(1, 6)
                    num_of_rolls = 0
                    rollingActive = False

            if camera.mouseclick:
                if final_roll is None:
                    rollingActive = True
                else:
                    miniGame = "ClickingRainbow"
                    currentIndex += final_roll
                    final_roll = None
                    rollingActive = False
                keys.clear()

            if pygame.K_RETURN in keys:
                miniGame = "ClickingRainbow"
                keys.clear()

            if pygame.K_RIGHT in keys:
                currentIndex += 1
                if currentIndex >= len(board_space_coords):
                    print("Game Won!")
                    currentIndex = 0
                    gamePaused = True

        if miniGame == "ClickingRainbow":  # minigame 1
            camera.clear('white')
            if pygame.K_w in keys:
                CRObjects[7][0].y -= 10
            if pygame.K_s in keys:
                CRObjects[7][0].y += 10
            if pygame.K_a in keys:
                CRObjects[7][0].x -= 10
            if pygame.K_d in keys:
                CRObjects[7][0].x += 10
            for object in CRObjects:
                if CRObjects[object][2] == False:
                    camera.draw(CRObjects[object][0])
                if CRObjects[7][0].touches(CRObjects[object][0]) and object != 7:
                    if CRObjects[object][1] == mouse1 + 1:
                        CRObjects[object][2] = True
                        mouse1 = mouse1 + 1
            if CRObjects[6][2] == True:
                miniGame = None
                for object in CRObjects:
                    CRObjects[object][2] = False
                mouse1 = 0
                keys.clear()
        if miniGame == "Maze":
            camera.clear('white')
            if pygame.K_w in keys:
                mazePlayer.y -= 10
            if pygame.K_s in keys:
                mazePlayer.y += 10
            if pygame.K_a in keys:
                mazePlayer.x -= 10
            if pygame.K_d in keys:
                mazePlayer.x += 10
            if mazePlayer.x < 0:
                mazePlayer.x = 0
            if mazePlayer.x > 1000:
                mazePlayer.x = 1000
            if mazePlayer.y < 0:
                mazePlayer.y = 0
            if mazePlayer.y > 700:
                mazePlayer.y = 700
            for wall in MazeObjects:
                camera.draw(wall)
                if mazePlayer.touches(wall):
                    mazePlayer.speedx = 0
                    mazePlayer.speedy = 0
                    mazePlayer.move_to_stop_overlapping(wall)
            camera.draw(mazePlayer)
            camera.draw(destination)
            if mazePlayer.touches(destination):
                miniGame = None
                keys.clear()




    camera.display()


ticks = 30
gamebox.timer_loop(ticks, tick)