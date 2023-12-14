import sys

def main():
    data = open(sys.argv[1]).read().strip().split('\n')
    data = [[int(v) for v in l.split()] for l in data]
    ans = 0

    for row in data:
        steps = [row[-1]]
        while 1:
            diffs = []
            for i in range(len(row)-1):
                diffs.append(row[i+1] - row[i])
            if len(set(diffs)) == 1:
                break
            row = diffs
            steps.append(diffs[-1])

        new = row[-1]-row[-2]
        for val in steps:
            new = new + val
        ans += new
    return ans
print(main())