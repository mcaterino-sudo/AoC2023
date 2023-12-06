def main():
    file = open("day3Input.txt", "r")
    
    vec = []
    res = 0
    special_characters = "!@#$%^&*()-+?_=,<>/"
    
    for line in file:
        vec.append(list(line))
    
    for i in range(len(vec)):
        j = 0
        while j < len(vec[i]):
            if vec[i][j].isnumeric():
                check = False
                num = ""
                while(vec[i][j].isnumeric() and j < len(vec[i])):
                    if not check:
                        for n in range(i - 1, i + 2):
                            for k in range(j - 1, j + 2):
                                if n > 0 and n < len(vec) and k > 0 and k < len(vec[i]):
                                    if vec[n][k] in special_characters:
                                        check = True
                                        break
                            if check:
                                break
                    num += vec[i][j]
                    j += 1
                if check:
                    res += int(num)
            j += 1
    print(res)
                    
main()