import re

def searchNum(x, y, numbers, schema, touchNum):
    touching = []
    for num in numbers[y]:
            if  num[0] <= x <= num[1]  :
                return num
    return 0 

def checkStars(schem, stars, numbers, y):
    total = 0
    for star in stars: # iterate through stars
        touchPos = []
        touchNum = []
        for i in range(-1, 2):  
            for j in range(-1, 2): # check surrounding swaure for digits
                if schem[star[1]+i][star[0]+j].isdigit(): # if square is digit
                    for num in numbers[star[1]+i]:
                        if num[0] <= star[0]+j <= num[1]:
                            numVal=schem[star[1]+i][num[0]:num[1]]
                            if not num in touchPos:
                                touchPos.append(num)
                                touchNum.append(numVal)
        if len(touchNum) == 2:
            product = int(touchNum[0]) * int(touchNum[1])
            total += product
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
    numbers = []
    stars = []
    while y < len(schematic):        
        iters = re.finditer(r'\d+', schematic[y])
        numList = []
        for i in iters:
            numList.append([i.span()[0],i.span()[1],y ])
        numbers.append(numList)

        iters = re.finditer(r'[*]', schematic[y])
        for i in iters:
            stars.append((i.span()[0],y))
        y += 1
    total = checkStars(schematic, stars, numbers, y) 
    print(total)
    return

main()