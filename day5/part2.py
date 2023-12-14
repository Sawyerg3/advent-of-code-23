import re
import sys

def convertToRanges(seeds):
    iterator = iter(seeds) # convert to iterator so zip() gets consecutive vals
    pairs = zip(iterator, iterator)
    seedRanges = []
    for s, r in pairs:
        seedRanges.append(range(s, s + r))
    return seedRanges

def main():
    data, *mappings = open(sys.argv[1]).read().strip().split("\n\n")
    seeds = data.split(':')[1].split()
    seeds = [int(seed) for seed in seeds ] 
    seeds = convertToRanges(seeds)
    
    for m in mappings:
        _, *ranges = m.split('\n')
        ranges = [[int(val) for val in r.split() ] for r in ranges]
        ranges = [(range(dest, dest+r), range(source, source + r)) for dest, source, r in ranges]
        new_seeds = []
        
        for r in seeds:
            for destRange, sourceRange in ranges:
                offset = destRange.start - sourceRange.start
                print("destRange:",destRange,"sourceRange:", sourceRange, "ranges:", ranges, 'r:', r, "offset:", offset)
                print()
                # if range not in source range
                if r.stop <= sourceRange.start or sourceRange.stop <= r.start:
                    # range stays same -> append(r)
                    continue

                ir = range(max(r.start, sourceRange.start), min(r.stop, sourceRange.stop))
                print(ir)
                lr = range(r.start, ir.start)
                rr = range(ir.stop, r.stop)
                print(lr)
                print(rr)
                if lr:
                    seeds.append(lr)
                if rr:
                    seeds.append(rr)
                new_seeds.append(range(ir.start + offset, ir.stop + offset))
                break
            else:
                new_seeds.append(r)

    print(min(x.start for x in new_seeds))
    return 
    
main()