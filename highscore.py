# Get High Score as Number
def getHighScore():
    with open("highscore.txt", "r") as hs:
        stats = hs.readlines()
    return stats


# Set High Score and Name
def setHighScore(name, score):
    with open("highscore.txt", "w") as hs:
        hs.write(name)
        hs.write("\n")
        hs.write(score)


# High Score Values
record = getHighScore()
highname = record[0]
highscore = int(record[1])
