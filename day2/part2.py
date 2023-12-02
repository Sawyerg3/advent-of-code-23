def calcPower(turns):
    colourCount = { "red" : 0, "green" : 0,  "blue" : 0 }
    for turn in turns:
        for colour in turn.split(","):
            colourNumber = colour.split()
            if (colourCount[colourNumber[1]] < int(colourNumber[0]) ):
                colourCount[colourNumber[1]] = int(colourNumber[0])

    return (colourCount["green"] * colourCount["blue"] * colourCount["red"])

def main():
    file = open("input.txt")
    line = file.readline()
    sum = 0
    
    while line != '': # EOF
        splitLine = line.split(":")
        sum += calcPower(splitLine[1].split(";"))
        line = file.readline()

    print(sum)
    return

main()