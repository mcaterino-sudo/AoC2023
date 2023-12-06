def main():
    file = open("day4test.txt", "r")
    
    res = 0
    
    for line in file:
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
        points = 0
        while i < len(line):
            if line[i].isnumeric():
                cur = line[i]
                i += 1
                while i < len(line) and line[i].isnumeric():
                    cur += line[i]
                    i += 1
                if cur in hashmap:
                    if not points:
                        points = 1
                    else:
                        points *= 2
            i += 1
        res += points
        
    print(res)
    
main()