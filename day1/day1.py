def lineValute(line):
    chars = len(line)
    value = ""
    x = 0
    while len(value) == 0 and x < chars:
        if line[x].isdigit():
            value = value + line[x]
        x += 1
    x = -1

    while len(value) == 1  and x >= -chars:
        if line[x].isdigit():
            value = value + line[x]
        x -= 1

    return int(value)


def main():
    file = open("input.txt")
    # file = open("test.txt")
    line = file.readline()

    sum = 0
    while line != '': # EOF
        sum += lineValute(line)
        line = file.readline()

    print(sum)
    return

main()
