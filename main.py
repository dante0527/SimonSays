import os
import random
import time
from highscore import *

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Simon's turn
def simon_says():
    global simons_colors
    simons_colors += random.choice(colors)
    for color in simons_colors:
        print("Simon says:")
        time.sleep(0.1)
        clear()

        print(f"Simon says: {color}")
        time.sleep(1)
        clear()

    return simons_colors


# Your turn
def user_turn():
    turn = input("Your turn:\n").upper()
    return turn


# Game info
colors = ('R', 'G', 'B', 'Y')
simons_colors = []
level = 1
score = 0

# Initialize game
for i in range(3):
    simons_colors += random.choice(colors)

# Game start
print("New Game")
time.sleep(2)
clear()
print(f"High Score: {highscore} by {highname}")
time.sleep(2)
clear()

while True:
    sequence = ''.join(simon_says())
    if user_turn() == sequence:
        score += 1
        level += 1
        clear()
    else:
        if score > highscore:
            clear()
            print(f"GAME OVER\nNew High Score: {score}!\nEnter your name: ")
            name = input()
            setHighScore(name, str(score))
            break
        else:
            clear()
            print(f"GAME OVER\nScore: {score}\nHigh Score: {highscore}")
            break
