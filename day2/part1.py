def checkTurn(turn):
    rules = {"green" : 13, "red" : 12, "blue" : 14 }
    colours = turn.split(",")
    for colour in colours:
        colourNumber = colour.split()
        if (rules[colourNumber[1]] < int(colourNumber[0]) ):
            return - 1

    return 1


def checkGame(game):
    splitGame = game.split(":")
    gameNumber = int(splitGame[0].split()[1])
    turns = splitGame[1].split(";")

    for turn in turns:
         if checkTurn(turn) == -1:
            return 0

    return gameNumber 


def main():
    file = open("input.txt")
    line = file.readline()
    sum = 0
    
    while line != '': # EOF
        sum += checkGame(line)
        line = file.readline()

    print(sum)
    return

main()