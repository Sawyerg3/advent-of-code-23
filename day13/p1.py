import sys

def checkReflect(m, i):
    top, bottom = m[:i], m[i+2:]

    for j in range(min(len(top), len(bottom))):
        if top[-(j+1)] != bottom[j]:
            return 0
    return 1


def transpose(m):
    return [''.join(c) for c in zip(*m)]


def main():
    data = open(sys.argv[1]).read().strip().split('\n\n')
    data = [i.split('\n') for i in data ]
    ans = 0

    for m in data:
        for i in range(len(m) - 1):
            if m[i] == m[i+1]:
                if checkReflect(m,i):
                    ans += (i+1) * 100
                    break
        m = transpose(m)
        for i in range(len(m) - 1):
            if m[i] == m[i+1]:
                if checkReflect(m,i):
                    ans += (i+1) 

    print(ans)
    return
main()

#20646  29846