from math import floor


def main():
    file = open("day6Input.txt", "r")
    
    times = []
    dists = []
    res = 1
    
    for line in file:
        if times == []:
            firstLine = line.split(':')
            firstLine[1] = firstLine[1].strip()
            times = firstLine[1].split(' ')
            newTimes = []
            for time in times:
                if time != '':
                    newTimes.append(time)
            times = newTimes
            time = ""
            for strs in times:
                time += strs
            time = int(time)
        else:
            secondLine = line.split(':')
            secondLine[1] = secondLine[1].strip()
            dists = secondLine[1].split(' ')
            newDists = []
            for dist in dists:
                if dist != '':
                    newDists.append(dist)
            dists = newDists
            dist = ""
            for strs in dists:
                dist += strs
            dist = int(dist)
    high = time//2
    low = 1
    while low < high:
        mid = (low + high)//2
        if (time - mid) * mid > dist:
            if (time - (mid - 1)) * (mid - 1) <= dist:
                lowTime = mid
                break
            high = mid - 1
        else:
            low = mid + 1
        if low == high:
            lowTime = low
    odd = 0
    if time % 2 != 0:
        odd = 1
    res *= ((time//2 - lowTime) + (time//2) + odd) - (lowTime - 1)
    print(res)

main()