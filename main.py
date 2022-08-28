import os
import random
import time
from highscore import *

# Clear Terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Show High Score
def showHighScore():
    print(f"High Score: {highscore} by {highname}")


# Show Player's Current Score
def showScore():
    print(f"Score: {score}")


# Add Color to Simon's Sequence
def simonSays():
    global simons_colors
    simons_colors += random.choice(colors)


# Your Turn
def userTurn():
    turn = input("Your turn:\n").upper()
    return turn


# Possible Colors in Sequence
colors = ('R', 'G', 'B', 'Y')

# Simon's Sequence
simons_colors = []

# Tracks Player's Score
score = 0

# Initialize Simon's Sequence
for i in range(2):
    simons_colors += random.choice(colors)

# Show High Score
clear()
showHighScore()
time.sleep(2)

# Show Player Score
clear()
showScore()
time.sleep(2)

# Gameplay Loop
while True:

    # Add Color to Sequence
    simonSays()

    # Combine Simon's Colors into Sequence
    sequence = ''.join(simons_colors)

    # Show Simon before printing sequence
    print("Simon says:")
    time.sleep(1)
    clear()
    showScore()

    # Show One Color at a Time
    for color in simons_colors:

        # Pause Between Colors
        print("Simon says:")
        time.sleep(0.1)
        clear()
        showScore()

        # Display Next Color
        print(f"Simon says: {color}")
        time.sleep(1)
        clear()
        showScore()

    # Correct Sequence from Player
    if userTurn() == sequence:

        # Increase Score
        score += 1
        clear()
        showScore()

    # Game Over
    else:

        # New High Score
        if score > highscore:

            # Display High Score Message
            clear()
            print(f"GAME OVER\nNew High Score: {score}!")

            # Get player's name
            name = input("Enter your name: ")

            # Save new high score
            setHighScore(name, str(score))
            break
        
        # No New High Score
        else:
            
            # Display Game Over Message
            clear()
            print("GAME OVER")

            # Show High Score
            showHighScore()

            # Show Player Score
            print(f"Score: {score}")
            break
