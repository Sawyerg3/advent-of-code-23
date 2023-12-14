import sys

def convertJ(hand):
    labels = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']

    if hand.count('J') == 3:
        for la in list(filter(lambda x: x != 'J', labels)):
            co = hand.count(la)
            if co == 2 : # 3 J + pair -> 5 of a kind
                return  7

    for l in labels:
        c = hand.count(l)
        if c==5:
            return 7
        elif c == 4  :
            return  7
        elif c == 3 :
            if hand.count('J') == 2:
                return 7
            return 6
        # Fullhouse, Three of a kind, Two pair, Best pair 
        elif c == 2 :
            for la in list(filter(lambda x: x != l, labels)):
                co =  hand.count(la)
                if co == 2 : # Two pair -> convert to fullhouse ****
                    elif la =='J' or l == 'J':
                        return  6 # 4 of kind
                    return 5 # full house 
            return 4
    # else  one pair
    return 2


def f(hand):
    labels = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
    score = 1

    if 'J' in hand:
        return(convertJ(hand))

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
            if score < 3: score = 2
    return score

def main():
    data = open(sys.argv[1]).read().strip().split('\n')
    labels = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
    labels.reverse()
    l = []
    for x in data:
        hand = x.split()[0]
        l.append((hand,[labels.index(i) for i in hand], int(x.split()[1]), f(hand) ))  # [(hand, handpos, bid, score)]

    l.sort(key=lambda x: (x[3],x[1]))
    ans = sum([(x+1)*i[2] for x,i in enumerate(l)])
    print(ans)
    return

main()

#250057090