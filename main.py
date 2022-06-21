import os
import random
import time

from highscore import *


# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def clearWithScore():
    os.system('cls' if os.name == 'nt' else 'clear')
    showScore()


def showHighScore():
    print(f"High Score: {highscore} by {highname}")


def showScore():
    print(f"Score: {score}")


# Simon's turn
def simon_says():
    global simons_colors
    simons_colors += random.choice(colors)
    for color in simons_colors:
        print("Simon says:")
        time.sleep(0.1)
        clearWithScore()

        print(f"Simon says: {color}")
        time.sleep(1)
        clearWithScore()

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
clear()
showHighScore()
time.sleep(2)
clearWithScore()
time.sleep(2)

while True:
    sequence = ''.join(simon_says())
    if user_turn() == sequence:
        score += 1
        level += 1
        clearWithScore()
    else:
        if score > highscore:
            clear()
            print(f"GAME OVER\nNew High Score: {score}!\nEnter your name: ")
            name = input()
            setHighScore(name, str(score))
            break
        else:
            clear()
            print("GAME OVER")
            showHighScore()
            print(f"Score: {score}")
            break
