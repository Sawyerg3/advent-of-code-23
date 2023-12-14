import sys


def checkSmudges(top,bottom):
    return sum(t!=b for t,b in zip(top,bottom))
    # smudges = 0
    # for t, b in zip(top, bottom):
        # smudges += t!=b
    # return smudges


def checkReflect(m):
    for i in range(1,len(m)):
        top, bottom = m[:i], m[i:]
        smudges = 0

        for j in range(min(len(top), len(bottom))):
            smudges += checkSmudges(top[-(j+1)], bottom[(j)] )
        if smudges == 1 : 
            return i
    return 0


def main():
    data = open(sys.argv[1]).read().strip().split('\n\n')
    data = [i.split('\n') for i in data ]
    ans = 0

    for m in data:
        if x := checkReflect(m):
                ans += x * 100
                continue
        m = [''.join(c) for c in zip(*m)]
        if x:= checkReflect(m):
            ans += x
    print(ans)
    return
main()

#31736 25401