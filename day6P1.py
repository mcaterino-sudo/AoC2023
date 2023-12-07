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
            times = [int(time) for time in times]
        else:
            secondLine = line.split(':')
            secondLine[1] = secondLine[1].strip()
            dists = secondLine[1].split(' ')
            newDists = []
            for dist in dists:
                if dist != '':
                    newDists.append(dist)
            dists = newDists
            dists = [int(dist) for dist in dists]
            
    for i in range(len(times)):
        high = times[i]//2
        low = 1
        while low < high:
            mid = (low + high)//2
            if (times[i] - mid) * mid > dists[i]:
                if (times[i] - (mid - 1)) * (mid - 1) <= dists[i]:
                    time = mid
                    break
                high = mid - 1
            else:
                low = mid + 1
            if low == high:
                time = low
        odd = 0
        if times[i] % 2 != 0:
            odd = 1
        print(time)
        #print(times[i]//2)
        res *= ((times[i]//2 - time) + (times[i]//2) + odd) - (time - 1)
        #print((times[i]//2 - time) + (times[i]//2) + odd - (time - 1))
    print(res)

main()