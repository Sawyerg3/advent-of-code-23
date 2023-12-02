def checkWordFront(line):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    temp, pos = 0, 0
    val, x = 0 , 0

    for num in numbers:
        x += 1
        temp = line.find(num) 
        if temp > -1 and (temp < pos or val == 0):
            pos = temp
            val = x

    return val, pos


def checkWordBack(line):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    temp, pos = 0, 0
    val, x = 0 , 0

    for num in numbers:
        x += 1
        temp = line.rfind(num) 
        if temp > -1 and (temp > pos or val == 0):
            pos = temp
            val = x

    return val, pos


def lineValue(line):
    chars = len(line)
    value = ""
    x = 0
    wordVal, wordPos = checkWordFront(line)

    while len(value) == 0 and x < chars:
        if line[x].isdigit():
            break
        x += 1

    if x - 1 > wordPos and wordVal != 0: 
        value = value + str(wordVal)
    else: 
        value = value + line[x]

    # Second digit:
    secondDigit = ""
    wordVal, wordPos = checkWordBack(line)

    x = -1
    while secondDigit == ""  and x >= -chars:
        if line[x].isdigit():
            secondDigit = secondDigit + line[x]
        x -= 1

    if wordPos > chars + x and wordVal != 0:
        value = value + str(wordVal)
    else:
        value = value + secondDigit

    return int(value)


def main():
    file = open("input.txt")
    # file = open("test.txt")
    line = file.readline()
    sum = 0
    
    while line != '': # EOF
        sum += lineValue(line)
        line = file.readline()

    print(sum)
    return

main()