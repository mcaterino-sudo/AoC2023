def main():
    file = open("day5Input.txt", "r")
    
    seeds = []
    
    for line in file:
        if seeds == []:
            firstLine = line.split(':')
            firstLine[1] = firstLine[1].strip()
            seeds = firstLine[1].split(' ')
            seeds = [int(seed) for seed in seeds]
            check = [0] * len(seeds)
            continue
        if line[0].isnumeric():
            dest, source, rangeLen = line.split(' ')
            dest, source, rangeLen = int(dest), int(source), int(rangeLen)
            for i, seed in enumerate(seeds):
                if (seed >= source) and (seed < (source + rangeLen)) and (check[i] == 0):
                    seeds[i] = (seed - source) + dest
                    check[i] = 1
        else:
            check = [0] * len(seeds)
    print(min(seeds))
main()