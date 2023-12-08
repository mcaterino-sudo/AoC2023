from math import gcd


def main():
    file = open("day8Input.txt", "r")
    
    instructions = ""
    hashmap = {}
    aNodes = []
    
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
            if node[-1] == 'A':
                aNodes.append(node)
    lcm = [0] * len(aNodes)
            
    count = 0
    while checkNodes(lcm):
        for char in instructions:
            count += 1
            for i in range(len(aNodes)):
                if char == 'L':
                    aNodes[i] = hashmap[aNodes[i]][0]
                else:
                    aNodes[i] = hashmap[aNodes[i]][1]
                if aNodes[i][-1] == 'Z' and lcm[i] == 0:
                    lcm[i] = count
    cur = (lcm[0] * lcm[1]) // gcd(lcm[0], lcm[1])
    for i in range(2, len(lcm)):
        cur = (cur * lcm[i]) // gcd(cur, lcm[i])
    print(cur)
        
    print(count)


def checkNodes(lcm):
    for num in lcm:
        if num == 0:
            return True
    return False
    

main()