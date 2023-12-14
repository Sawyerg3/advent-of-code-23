import sys
from math import gcd

def main():
    data = open(sys.argv[1]).read().strip().split('\n')
    lr = data[0]
    data = data[2:]
    d = {}
    for x in data:
        d[x[0:3]] = [x[7:10], x[12:15]]

    s = []
    for k,v in d.items():
        if 'A' == k[2]:
            s.append(k)

    z_steps = []
    for val in s:
        i = 0
        while 1 :
            if i == len(lr): lr = lr+lr
            if val[2] == 'Z':
                z_steps.append(i)
                break
            if lr[i] == 'L':
                val = d[val][0]
            else: 
                val = d[val][1]   
            i+=1

    ans = 1
    for i in z_steps:
        ans = (i*ans)//gcd(i,ans)
    print(ans)
    return
main()