def main():
    file = open("day3Input.txt", "r")
    
    vec = []
    res = 0
    
    for line in file:
        vec.append(list(line))
    
    for i in range(len(vec)):
        j = 0
        while j < len(vec[i]):
            if vec[i][j] == '*':
                check = True
                num1 = 0
                num2 = 0
                for n in range(i - 1, i + 2):
                    for k in range(j - 1, j + 2):
                        if n >= 0 and n < len(vec) and k >= 0 and k < len(vec[i]):
                            if vec[n][k].isnumeric():
                                num = getNum(vec, n, k)
                                if num1 == 0:
                                    num1 = num
                                elif num2 == 0 and num != num1:
                                    num2 = num
                                elif num != num1 and num != num2:
                                    check = False
                if num1 and num2 and check:
                    print(num1, num2)
                    res += int(num1) * int(num2)
            j += 1
    print(res)

def getNum(vec, n, k):
    cur = k
    num = vec[n][k]
    k -= 1
    while k >= 0 and vec[n][k].isnumeric():
        num = vec[n][k] + num
        k -= 1
    k = cur + 1
    while k < len(vec[n]) and vec[n][k].isnumeric():
        num += vec[n][k]
        k += 1
    return num
                    
main()