# alterante solution for part 1
import sys

def main():
    data = open(sys.argv[1]).read().strip()
    _, seeds = data.split("\n\n")[0].split(":")
    seeds = [int(x) for x in seeds.split()]

    mappings = []
    data = data.split('\n\n')[1:]
    data = [i.split('\n') for i in data]
    mappings = [i[1:] for i in data]
    
    for m in mappings:
        updateVals = []
        for seed in seeds:
            inRange = False
            for i in m:
                i = [int(x) for x in i.split()]
                d, s, r = i
                if s <= seed <= s+ r:
                    inRange = True
                    updateVals.append(d + (seed - s))
                    break 
            if not inRange: updateVals.append(seed)        
        seeds = updateVals

    print(min(seeds))
    return

main()