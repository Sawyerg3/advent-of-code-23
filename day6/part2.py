import math

def f1(t,d):
    total = 0
    for h in range(t):
        if h * (t - h) > d:
            total += 1   
    return

# alt solution
def f2(t,d):
    a = (t - math.sqrt(t**2 - 4 *d) ) // 2
    b = (t + math.sqrt(t**2 - 4 *d) ) // 2
    return b - a

def main():
    t , d =  34908986, 204171312101780
    total = f1(t,d)
    # total = f2(t,d)
    print(total)
    
main()
# 20048741