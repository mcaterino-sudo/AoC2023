def main():
    file = open("day4Input.txt", "r")
    
    cards = [1] * 204
    
    curCard = 0
    
    for line in file:
        matches  = getMatches(line)
        for i in range(curCard + 1, curCard + matches + 1):
            cards[i] += cards[curCard]
        curCard += 1
    print(sum(cards))        

def getMatches(line):
    hashmap = {}
    i = 9
    while line[i] != '|':
        if line[i].isnumeric():
            cur = line[i]
            i += 1
            while line[i].isnumeric():
                cur += line[i]
                i += 1
            hashmap[cur] = 0
        i += 1
    matches = 0
    while i < len(line):
        if line[i].isnumeric():
            cur = line[i]
            i += 1
            while i < len(line) and line[i].isnumeric():
                cur += line[i]
                i += 1
            if cur in hashmap:
                matches += 1
        i += 1
    return matches
    
main()