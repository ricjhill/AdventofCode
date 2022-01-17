# --- Day 7: The Treachery of Whales ---
#
# A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!
#
# Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!
#
# The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?
#
# There's one major catch - crab submarines can only move horizontally.
#
# You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.
#
# For example, consider the following horizontal positions:
#
# 16,1,2,0,4,2,7,1,2,14
#
# This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.
#
# Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:
#
#     Move from 16 to 2: 14 fuel
#     Move from 1 to 2: 1 fuel
#     Move from 2 to 2: 0 fuel
#     Move from 0 to 2: 2 fuel
#     Move from 4 to 2: 2 fuel
#     Move from 2 to 2: 0 fuel
#     Move from 7 to 2: 5 fuel
#     Move from 1 to 2: 1 fuel
#     Move from 2 to 2: 0 fuel
#     Move from 14 to 2: 12 fuel
#
# This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).
#
# Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

# Nice solution
# https://www.ericburden.work/blog/2021/12/07/advent-of-code-2021-day-7/
# This was less a programming challenge than a math/logic challenge. If it’s not clear why the median of the array of crab positions is the right value for them to line up on, consider the following sequence (our example) in order:
# 0, 1, 1, 2, 2, 2, 4, 7, 14, 16
#              ^
#            median
# It makes intuitive sense that the optimal position should be somewhere near the middle, and there’s nowhere more “middle” than the median. A mean, or average, can be influence by large outlier values, but not the median. With this intuition in hand, try to come up with an example where the median wouldn’t be the right answer. I couldn’t, but maybe you’re more creative than I am.


# Part 1
from pathlib import Path
import statistics


input_data: list[int] = list(map(int, Path('day7_input.txt').read_text().rstrip().split(',')))


#  ok so this works and it is concise.. but I  have no idea what  it  does.
fuel_cost = { x: sum([  abs(x - z) for z in input_data]  ) for x in range(0, max(input_data) + 1) }
#print(fuel_cost)
print(min(fuel_cost.values()))

#  But lets use the median

print(input_data)
median = statistics.median(input_data)

target = median
fuel = 0

for distance in input_data:
    fuel = fuel + abs(target - distance)
    #print("fuel: " + str(fuel) + "     distance: " + str(distance))

print(fuel)

print("Part 2")

""" There are  at  least  two ways  to solve this problem, we  can either brute force it  or  use gauss technique for 
finding the average in an arithmetric series.  This involves  finding the  round(mean - 0.5) and round(mean + 0.5) and 
choosing the lowest  as the answer.

https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/
"""

"""
--- Part Two ---

The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal 
position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 
3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all 
on; in the example above, this becomes 5:

    Move from 16 to 5: 66 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 0 to 5: 15 fuel
    Move from 4 to 5: 1 fuel
    Move from 2 to 5: 6 fuel
    Move from 7 to 5: 3 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 14 to 5: 45 fuel

This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 
fuel instead.

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an 
escape route! How much fuel must they spend to align to that position?

"""

# Find the full range covered by  the crabs.
min_pos = min(input_data)
max_pos = max(input_data)

# Populate total fuel cost to move everything to each position
fuel = []
for pos in range(min_pos, max_pos + 1):
    fuel.append(0)
    for crab in input_data:
        fuel[-1] += sum(range(abs(crab - pos) + 1))
# Print minimum cost
print(min(fuel))
