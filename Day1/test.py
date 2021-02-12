stations = [1, 2, 1, 5, 2, 2, 2, 5, 3, 4, 4, 4, 4, 5, 3, 4, 4]


# list(map(int, input().rstrip().split()))
def findMax(lst):
    maxOrigin = []
    for i in lst:
        if len(i) > len(maxOrigin):
            maxOrigin = i
    return maxOrigin


def origin(stations):
    origins = []
    for i in range(len(stations) - 1):
        for j in range(len(stations) - 1, i, -1):
            if stations[i] == stations[j]:
                originStations = stations[i:j + 1]
                origins.append(originStations)

    way = findMax(origins)
    return way


way = origin(stations)

print(way)
