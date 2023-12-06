def main():
    file = open("day2Input.txt", "r")
    
    res = 0
    
    for line in file:
        gameID = 0
        r = 0
        g = 0
        b = 0
        for i in range(len(line)):
            if line[i].isnumeric():
                cur = ""
                while(line[i].isnumeric()):
                    cur += line[i]
                    i += 1
                if gameID == 0:
                    gameID = cur
                    continue
                match line[i + 1]:
                    case 'r':
                        r = max(r, int(cur))
                    case 'g':
                        g = max(g, int(cur))
                    case 'b':
                        b = max(b, int(cur))
        res += (r * g * b)
    print(res)
    
main()