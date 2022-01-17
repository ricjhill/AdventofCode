import collections
import sys

ages = sys.stdin.read()
# If receiving error mapping input, add a return before ending input stream
fishies = list(map(int, ages.split(',')))
# Create a deque that will hold number of fish with a timer equivalent to
# their index w/in the deque
totals = collections.deque(fishies.count(i) for i in range(9))
# Loop over all 256 days
for _ in range(256):
    # Rotate all timers down one for the day and add in the parents
    # of the newly added fish to the parents timer slot of 6
    totals.rotate(-1)
    totals[6] += totals[8]
print(sum(totals))