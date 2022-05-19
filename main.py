import os
import random
import time


# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Simon's turn
def simon_says():
    simons_colors = []
    for i in range(level + 3):
        color = random.choice(colors)
        simons_colors += color
        print(f"Simon says:\n{color}")
        time.sleep(level)
        clear()
    return simons_colors


# Your turn
def user_turn():
    turn = input("Your turn:\n")
    return turn


colors = ('R', 'G', 'B', 'Y')
level = 1
score = 0

while True:
    print("Simon says:")
    simon_says()
    if user_turn() == simon_says():
        score += 1
        level += 1
