def main():
    file = open("day1Input.txt", "r")
    
    res = 0
    
    for line in file:
        start = 0
        end = len(line) - 1
        num1 = ''
        num2 = ''
        
        while ((not num1) or (not num2)):
            if line[start].isnumeric():
                if not num1:
                    num1 = line[start]
                    
            if line[end].isnumeric():
                if not num2:
                    num2 = line[end]
            start += 1
            end -= 1
            
        num = num1 + num2
        res += int(num)
        
    print(res)
    
    file.close()

if __name__ == main():
    main()
