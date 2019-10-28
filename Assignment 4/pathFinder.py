################################
#
#     Computer Science 220
#  Assignment 4 | Path Finder
#
#    Writed By Dan Richards
#  Almost as fast as the F2004
#Code Inspried by Geeks for Geeks
# 
################################

from sys import stdin, stdout
from math import sin, cos, sqrt, atan2, radians
import copy
import collections

cases = int(stdin.readline())
radius = 6371

for caseIndex in range(0, cases):
    numberOfCities = int(stdin.readline())
    defaultDict = dict.fromkeys(range(numberOfCities))
    cityData = copy.copy(defaultDict)
    for i in range(0, numberOfCities ):
        lineData = stdin.readline().strip().split()
        cityData[i] = list()
        cityData[i].append(lineData[0])
        cityData[i].append(lineData[1])
        cityData[i].append(" ".join(lineData[2:]))

    fuel = float(stdin.readline())
    matrix = {k: copy.copy(defaultDict) for k in range(numberOfCities)}
    for i in range(0, numberOfCities):
        lat1 = radians(float(cityData[i][0]))
        long1 = radians(float(cityData[i][1]))
        cityName1 = cityData[i][2] 
        for j in range(0, numberOfCities):
            if i != j and matrix[i][j] == None:
                lat2 = radians(float(cityData[j][0]))
                long2 = radians(float(cityData[j][1]))
                cityName2 = cityData[j][2]
                latDelta = lat2 - lat1
                longDelta = long2 - long1
                a = (sin(latDelta/ 2)** 2) + cos(lat1) * cos(lat2) * (sin(longDelta / 2) ** 2)
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                d = radius * c  
                if d <= fuel:
                    matrix[i][j] = d 
                    matrix[j][i] = d
                else:
                    matrix[i][j] =  float("Inf") 
                    matrix[j][i] =  float("Inf") 

    #Dijkstras Begins Here

    distance = {k:float("Inf") for k in range(numberOfCities)}
    parent = {k:-1 for k in range(numberOfCities)}
    distance[0] = 0 
    dijkstraQueue = []

    #Add Cities
    for i in range(0, numberOfCities):
        dijkstraQueue.append(i)

    #Go through queue
    while len(dijkstraQueue) > 0:
        minimumDistanceValue = float("Inf")
        minimumDistanceIndex = -1

        for i in range(len(distance) ):
            if i in dijkstraQueue and distance[i] < minimumDistanceValue: 
                minimumDistanceValue = distance[i]
                minimumDistanceIndex = i
                u = minimumDistanceIndex 
        try:
            dijkstraQueue.remove(minimumDistanceIndex)
        except:
            break
        for i in range(0, numberOfCities):
            if i in dijkstraQueue and matrix[u][i]:
                if distance[u] + matrix[u][i] < distance[i]:
                    parent[i] = u
                    distance[i] = distance[u] + matrix[u][i]
    if parent[numberOfCities - 1] == -1:
        print("Not possible")
        continue
    cityList = collections.deque()
    index = numberOfCities - 1 
    printKey = True
    while printKey:
        if index == -1:
            printKey = False
            break
        cityList.append(cityData[index][2:])
        index = parent[index]
    for i in range(0, len(cityList) -1):
        stdout.write(str(cityList.pop()[0]))
        stdout.write(", ")
   
    stdout.write(str(cityList.pop()[0]))
    stdout.write("\n")


