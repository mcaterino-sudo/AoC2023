def main():
    file = open("day2Input.txt", "r")
    
    res = 0
    
    for line in file:
        gameID = 0
        for i in range(len(line)):
            check = True
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
                        if int(cur) > 12:
                            check = False
                            break
                    case 'g':
                        if int(cur) > 13:
                            check = False
                            break
                    case 'b':
                        if int(cur) > 14:
                            check = False
                            break
        if check:
            res += int(gameID)
    print(res)
    
main()