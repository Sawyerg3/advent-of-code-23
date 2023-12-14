import sys

def main():
    data = open(sys.argv[1]).read().strip().split('\n')
    lr = data[0]
    data = data[2:]
    d = {}
    for x in data:
        d[x[0:3]] = [x[7:10], x[12:15]]

    i = 0
    a = 'AAA'
    while 1:
        if i == len(lr): lr = lr+lr
        if a == 'ZZZ':
            return
        if lr[i] == 'L':
            a = d[a][0]
        else: 
            a = d[a][1]   
        i+=1
    return
main()
#15989