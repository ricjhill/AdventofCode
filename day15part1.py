"""
--- Day 15: Chiton ---
You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581

You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

[1] 1  6  3  7  5  1  7  4  2
[1] 3  8  1  3  7  3  6  7  2
[2][1][3][6][5][1][1] 3  2  8
 3  6  9  4  9  3 [1][5] 6  9
 7  4  6  3  4  1  7 [1] 1  1
 1  3  1  9  1  2  8 [1][3] 7
 1  3  5  9  9  1  2  4 [2] 1
 3  1  2  5  4  2  1  6 [3] 9
 1  2  9  3  1  3  8  5 [2][1]
 2  3  1  1  9  4  4  5  8 [1]

The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?
"""
from collections import defaultdict
from pathlib import Path
import heapq

input_data: list[int] =  list(Path('input.txt').read_text().rstrip().split('\n'))
cmap = [[int(i) for i in line ] for line in Path('day15_input.txt').read_text().rstrip().split('\n')]


print(cmap)

pq = [(0, 0, 0)]
heapq.heapify(pq)
visited = set()
cost = defaultdict(int)

N = len(cmap)
M = len(cmap[0])

while len(pq) > 0:
    c, row, col = heapq.heappop(pq)

    if (row, col) in visited:
        continue
    visited.add((row, col))

    cost[(row, col)] = c

    if row == N -1 and col == M - 1:
        break

    for dr, dc in [(0,1),(0,-1),(1,0),(-1 ,0),]:
        rr =  row + dr
        cc = col + dc
        if not (0 <= rr < N and 0 <= cc < M):
            continue

        heapq.heappush(pq, (c + cmap[rr][cc], rr, cc))


print(cost[N-1, M-1])