import re

def searchForSymbol(schem, idx, y):
    a,b = -1,2 
    c,d = -1,2 

    if y == 0:
        a = 0
    if y == len(schem) - 1:
        b = 1
    if idx == 0:
        c = 0
    if idx == (len(schem[0]) - 1):
        d = 1

    for i in range(a, b):
        for j in range(c, d):
            # print(schem[y+i][idx+j], end='')
            char = schem[y+i][idx+j]
            if not (char.isdigit() ) and char != '.': 
                return True
    return False


def checkNumbers(schem, nums, y):
    total = 0   
    for i, n in nums.items():
        for j in range(len(n)): # for each digit in number
            if searchForSymbol(schem, i + j, y):
                total += int(n)
                break
    return total


def main():
    file = open("input.txt")
    # file = open("test.txt")    
    total = 0
    schematic = []

    line = file.readline()
    while line != '': # EOF
        schematic.append(line.strip('\n'))
        line = file.readline()

    y =  0
    while y < len(schematic):
        numbers = {}
        iters = re.finditer(r'\d+', schematic[y])
        for i in iters:
            numbers[i.span()[0]] = i.group()
        total += checkNumbers(schematic, numbers, y)
        y += 1      
    print(total)
    return

main()