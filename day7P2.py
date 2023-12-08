def getRank(hand):
    pos = [0] * 13
    
    for card in hand:
        match card:
            case '2':
                pos[0] += 1
            case '3':
                pos[1] += 1
            case '4':
                pos[2] += 1 
            case '5':
                pos[3] += 1     
            case '6':
                pos[4] += 1    
            case '7':
                pos[5] += 1    
            case '8':
                pos[6] += 1   
            case '9':
                pos[7] += 1   
            case 'T':
                pos[8] += 1    
            case 'J':
                pos[9] += 1
            case 'Q':
                pos[10] += 1                
            case 'K':
                pos[11] += 1 
            case 'A':
                pos[12] += 1
    pair = 0
    trip = 0
    four = 0
    for i in range(len(pos)):
        match pos[i]:
            case 2:
                pair += 1
            case 3:
                trip += 1
            case 4:
                four += 1
            case 5:
                return 7
    joker = pos[9]
    if four:
        if joker:
            return 7
        return 6
    if pair and trip:
        if joker:
            return 7
        return 5
    if trip:
        if joker:
            return 6
        return 4
    if pair == 2:
        if joker == 2:
            return 6
        if joker:
            return 5
        return 3
    if pair:
        if joker:
            return 4
        return 2
    if joker:
        return 2
    return 1
            
def compare(hand1, hand2):
    rank1 = getRank(hand1)
    rank2 = getRank(hand2)
    
    if rank1 > rank2:
        return True
    elif rank2 > rank1:
        return False
    else:
        for i in range(len(hand1)):
            val1 = hand1[i]
            if val1 == 'A':
                val1 = 14
            if val1 == 'K':
                val1 = 13
            if val1 == 'Q':
                val1 = 12
            if val1 == 'J':
                val1 = 1
            if val1 == 'T':
                val1 = 10
            val1 = int(val1)
            val2 = hand2[i]
            if val2 == 'A':
                val2 = 14
            if val2 == 'K':
                val2 = 13
            if val2 == 'Q':
                val2 = 12
            if val2 == 'J':
                val2 = 1
            if val2 == 'T':
                val2 = 10
            val2 = int(val2)
            if val1 > val2:
                return True
            if val2 > val1:
                return False
    
def partition(hands, low, high):
    i = low - 1
    
    for j in range(low, high):
        if compare(hands[high][0], hands[j][0]):
            i = i + 1
            (hands[i], hands[j]) = (hands[j], hands[i])
    
    (hands[i + 1], hands[high]) = (hands[high], hands[i + 1])
    return i + 1
    
def quickSort(hands, low, high):
    if low < high:
        pivot = partition(hands, low, high)
        quickSort(hands, low, pivot - 1)
        quickSort(hands, pivot + 1, high)


def main():
    file = open("day7Input.txt", "r")
    
    hands = []
    
    for line in file:
        strip = line.strip()
        split = strip.split(' ')
        hands.append([split[0], split[1]])
    quickSort(hands, 0, len(hands) - 1)
    res = 0
    for i in range(len(hands)):
        res += int(hands[i][1]) * (i + 1)
    print(res)

main()