# ShortestPathAlgorithmWithMaxWeight
An algorithm that finds the shortest path between two nodes in a graph with a specified maximum weight. 

## Usage
You can use this program of when you want to find the shortest distance between two places (With given coordinates) with the condition that when moving between the nodes you cannot move more than a specified amount. 
The program will also specify if the path cannot be made. For example trying to go between London and Auckland with 300km of fuel. 

## Input 
``` 
2                                 - Number of graphs or exercises to perform
8                                 - Number of nodes in graph (Order)
-36.8533 174.749 Auckland         - Latitude, Longitude, City
-37.788 175.265 Hamilton
-37.7012 176.154785 Tauranga
-38.677 176.0669 Taupo
-39.926 175.045 Wanganui
-39.4956 176.9 Napier
-40.3465 175.6055 Palmerston North
-41.2943 174.7595 Wellington
300                               - Max distance between cities
2     
48.4275 -123.367259 Victoria      
44.653 -63.588867 Halifax
1000
```

## Output
```
Auckland, Hamilton, Wanganui, Wellington
Not possible
A, C, Z
A, D, F, Z
A, D, H, E, Z
St. John, St. Michael
Not possible
```


## Running the program
```
python3 pathFinder.py < input.txt > output.txt
or to print output on screen
python3 pathFinder.py < input.txt
```


