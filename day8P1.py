def main():
    file = open("day8Input.txt", "r")
    
    instructions = ""
    hashmap = {}
    
    for line in file:
        if instructions == "":
            instructions = line.strip()
        elif line == "\n":
            continue
        else:
            temp = line.split(" = ")
            node = temp[0]
            temp = temp[1].strip()
            temp = temp.split(',')
            hashmap[node] = [temp[0][1:], temp[1][1:4]]
            
    cur = "AAA"
    count = 0
    while cur != "ZZZ":
        for char in instructions:
            count += 1
            if cur == "ZZZ":
                break
            elif char == 'L':
                cur = hashmap[cur][0]
            else:
                cur = hashmap[cur][1]
    print(count)
            
main()