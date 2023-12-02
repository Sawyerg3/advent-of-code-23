def lineValute(line):
    chars = len(line)
    value = ""
    x = 0
    while len(value) == 0 and x < chars:
        if line[x].isdigit():
            value = value + line[x]
        x += 1
    # print("value:" , value)
    x = -1
    # print(-x)

    while len(value) == 1  and x >= -chars:
        # print("loop")
        # print(line[x])
        if line[x].isdigit():
            value = value + line[x]
        x -= 1


    '''
    while len(value) == 1  and (chars - y != x):
        # print("loop")
        print(line[chars - y])
        if line[chars - y].isdigit():
            value = value + line[chars - y]
        y += 1 '''
    
    print(value)
    return int(value)


def main():
    file = open("input.txt")
    # file = open("test.txt")
    line = file.readline()
    # line = file.readline()
    # line = file.readline()


    sum = 0
    while line != '': # EOF
        sum += lineValute(line)
        # print('Reading:', line)
        line = file.readline()

    print(sum)
    # calibrationDoc = file.read()
    # print(calibrationDoc)

    return

main()
