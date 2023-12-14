import sys

def f(hand):
    labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3',  '2']
    score = 1

    for l in labels:
        c = hand.count(l)
        if c==5:
            return 7
        elif c == 4  :
            return 6
        elif c == 3 :
            for la in list(filter(lambda x: x != l, labels)):
                co =  hand.count(la)
                if co == 2 and score < 5:
                    return 5
            if score < 5:
                score = 4
        elif c == 2 :
            for la in list(filter(lambda x: x != l, labels)):
                co =  hand.count(la)
                if co == 2 and score < 3:
                    return 3
            if score< 3:score = 2
    return score

def comp(a,b):
    labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3',  '2']
    for i in range(len(a)):
        if labels.index(a[i]) > labels.index(b[i]):
            return 1
        elif labels.index(a[i]) < labels.index(b[i]):
            return 0
    return 0

def c(a,b):
    a1, b1,= f(a),f(b)
    if a1 > b1:
        return 0
    elif a1 < b1:
        return 1
    return comp(a, b) 
    
def sortFunc(l):
    for i in range(1,len(l)):
        curr = l[i]
        pos = i
        while pos > 0 and c(l[pos - 1],curr):
            l[pos] = l[pos-1]
            pos = pos -1
        l[pos] = curr
    return l

def main():
    data = open(sys.argv[1]).read().strip().split('\n')
    scores = []
    d = {}
    for x in data:
        d[x.split()[0]] =  x.split()[1]
    data = [x.split()[0] for x in data]
    
    ranks = sortFunc(data)
    total = 0
    for i in range(len(ranks)):
        total += int(d[ranks[i]]) * (len(ranks)-i)
  
    print(total)
    return
main()

#248812215