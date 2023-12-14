import re
import sys

def getMappedNum(sources, d, s, r, dest, source):
    for seed in sources:
        if dest in seed or dest == 'seed':
            pass
        elif s <= seed[source] <= s + r:
            seed[dest] = d + (seed[source] - s)

    return sources


def main():
    data = open(sys.argv[1]).read().strip()
    data = data.split('\n')
    data = [line for line in data if line]
    seeds = []

    for seed in re.findall(r'\d+', data[0]):
        seeds.append({'seed': int(seed)})
    data = data[1:]

    count = 1
    m = []
    for line in data:
            
        if line[0].isalpha():
            for seed in seeds:
                if len(seed) != count:
                    seed[dest] = seed[source]
            count += 1
            line = line.split()
            source, dest = line[0].split("-to-")
     
        elif line[0].isdigit():
            line = line.split() # destination, source, range
            line = [int(val) for val in line ]
            m.append(line)
            seeds = getMappedNum(seeds, line[0], line[1], line[2], dest, source)

    ans = list(seeds[0].values())[-1]
    for i in seeds:
        if list(i.values())[-1] < ans:
            ans = list(i.values())[-1]
    print(ans)
    return
    
main()