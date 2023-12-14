import sys
from itertools import combinations

def main():
    data = open(sys.argv[1]).read().strip().split('\n')
    ans = 0
    galaxies = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                galaxies.append((i,j))

    empty_row = [i for i, row in enumerate(data) if '#' not in row]
    empty_col = []
    for i in range(len(data[0])):
        empty = True
        for j in range(len(data)):
            if data[j][i] == '#':
                empty = False
        if empty:
            empty_col.append(i) 

    pairs = combinations(galaxies,2)
    for a,b in pairs:
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        expand = 0
        for i in empty_row:
            if i in range(min(a[0], b[0]), max(a[0],b[0])):
                expand += 1
        for i in empty_col:
            if i in range(min(a[1], b[1]), max(a[1],b[1])):
                expand += 1
        ans += dx + dy + expand

    print(ans)
    return
main()
