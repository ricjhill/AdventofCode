"""
-- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.
If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).
Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:
2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.
Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)
In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.
The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.
Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?
"""
from pathlib import Path


input_data: list[str] = list(Path('day9_input.txt').read_text().rstrip().split('\n'))
heightmap = [ [int(x) for x in row if x.isdigit()] for row in input_data]
print(heightmap)

def isLowPoint(row, column, grid):
    max_row = len(grid)
    max_col = len(grid[0])
    current_location_value = grid[row][column]
    possible_neighbors = []
    # populate the (row, col) of all adjacent locations - no diagonals though
    for i in (row - 1, row + 1):
        possible_neighbors.append((i, column))
    for j in (column - 1, column + 1):
        possible_neighbors.append((row, j))
    # x below is a (row, col) tuple for neighbors around the location in question
    # filter is used to avoid IndexErrors from going outside the matrix edges
    neighbors = list(filter(lambda x: 0 <= x[0] < max_row and 0 <= x[1] < max_col, possible_neighbors))
    neighbor_values = [grid[y][x] for (y, x) in neighbors]
    return current_location_value < min(neighbor_values)


def find_risk(hmap):
    total_risk = 0
    # keep track of the low points
    lowpoints = []
    for i, row in enumerate(hmap):
        for j, col in enumerate(row):
            if isLowPoint(i, j, hmap):
                lowpoints.append((i, j))
                # risk value of a low point is 1 plus its height
                total_risk += (1 + col)
    return total_risk, lowpoints

risk, low = find_risk(heightmap)
# print(risk)

"""
--- Part Two ---

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

21 99943210
3 987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:

21999 43210
398789 4 9 21
985678989 2
8767896789
9899965678

The middle basin, size 14:

2199943210
39 878 94921
9 85678 9892
87678 96789
9 8 99965678

The bottom-right basin, size 9:

2199943210
3987894921
9856789 8 92
876789 678 9
98999 65678

Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

"""


def getvalue(data, point):
    if (point[0] < 0) or (point[0] >= len(data)):
        return 10
    if (point[1] < 0) or (point[1] >= len(data[0])):
        return 10
    return data[point[0]][point[1]]


basins = []
for x in range(len(heightmap)):
    for y in range(len(heightmap[0])):
        count = 0
        open = [[x,y]]
        closed = []
        # print( open )
        while len(open) > 0:
            if (open[0] not in closed) and getvalue(heightmap, open[0]) < 9:
                count += 1
                closed.append(open[0])
                xx = open[0][0]
                yy = open[0][1]
                for element in [[xx+1,yy],[xx-1, yy], [xx, yy+1], [xx, yy-1]]:
                    open.append(element)
            del(open[0])
        for element in closed:
            heightmap[element[0]][element[1]] = 9
        if count > 0:
            basins.append(count)

basins = sorted(basins, reverse=True)
print( basins[0] * basins[1] * basins[2] )