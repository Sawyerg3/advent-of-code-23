import re
import sys

def main():
    cards = open(sys.argv[1]).read().strip()
    cards = cards.split('\n')
    cards = [ card[card.find(':')+2:]  for card in cards]  # cut all before semicolon
    points = 0
    for card in cards:
        groups = card.split('|')
        h1, h2 = re.findall(r'\d+', groups[0]), re.findall(r'\d+', groups[1])
        matches = len(set(h1) & set(h2))
        cardScore = 0
        if matches > 0: 
            points += 2**(matches-1)
    print(points)

main()
#19855