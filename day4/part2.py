import re
import sys
from collections import defaultdict
def main():
    cards = open(sys.argv[1]).read().strip()
    cards = cards.split('\n')
    games = defaultdict(int)

    for pos, card in enumerate(cards):
        games[pos] += 1
        numbers = card[card.find(':')+2:]
        hands = numbers.split('|')
        h1, h2 = re.findall(r'\d+', hands[0]), re.findall(r'\d+', hands[1])
        matches = len(set(h1) & set(h2))
        for i in range(matches):
            games[pos + 1 + i] += games[pos]

    print(sum(games.values()))

main()