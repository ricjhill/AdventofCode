"""
--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.
As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.
Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....
  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.
The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)
So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.
For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.
For example, here is what you might see in a single entry in your notes:
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)
Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.
Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.
For now, focus on the easy digits. Consider this larger example:
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).
In the output values, how many times do digits 1, 4, 7, or 8 appear?
"""

# Part 1
from pathlib import Path
from itertools import permutations

input_data: list[str] = list((Path('input.txt').read_text().rstrip().split('\n')))
data: list[tuple[str]] = [(left, right) for left, right in [ line.split(' | ') for line in input_data]]


outputs = [word[1] for word in data]
signals = [word[0] for word in data]


print("Part 1 -Proof")
total = 0
for line in outputs:
    for word in line.split():
        if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
            total += 1
print(total)


print("Part 2 -Proof")

def find_digits():
    """
    Step 0) Sort  and  group by length.

    Step 1) Some digits are easy to identify  because they have a unique number of segments:

    Digits with length two char  is "1"
    Digits with length three char  is "7"
    Digits with length four char  is "4"
    Digits with length seven char  is "8"


    Step 2) If the length of the digit is six char then the digit can be either "0","6","9". So we  need to subtract the
    two chars used in digit "1". If this can be done with one digit remaining then that  digit is "6".

    Step 3) We have digits "0" and  "9" remaining. The digit "4" contains the same segments as digit "9" but
    the digit "0" does not. So from "0" and "9", "0" is the digit which  does not contain  the middle segment.

    Step 4)  We now know digits "0","6","9" which are the six char digits. We  need to look at the five char
    digits, "2","3" and "5". All the chars from "6" are in "5"

    Step 5) With "2" and "3" remaining we can see that "3" contains the same char as "1" and "2" does not.

    """
    pass

def find1(arr: list)-> str:
    return [item for item in arr if len(item) == 2]


def find7(arr: list)-> str:
    return [item for item in arr if len(item) == 3]


def find4(arr: list)-> str:
    return [item for item in arr if len(item) == 4]


def find8(arr: list)-> str:
    return [item for item in arr if len(item) == 7]


def find(arr: list)-> str:
    return [find1(item) for item in arr]


def map_digits_to_numb_segments(num):
    mapping = {
    "1": 2,
    "2": 5,
    "3": 2,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "0": 6,
    }
    return mapping.get(num,"Invalid input")

print(map_digits_to_numb_segments("1"))
print(map_digits_to_numb_segments(0))







def sortString(str):
    return ''.join(sorted(str))



sorted_outputs = []
sorted_signals = []


# sort letters in the patterns  and put  them in a new list.
def sort_list_elements_alphabetically(unsorted_elements_list):
    x_sorted_outputs = []
    for line in unsorted_elements_list:
        for word in line.split(" "):
            new_word = ''.join(sorted(word))
            x_sorted_outputs.append(new_word)
    return x_sorted_outputs

sorted_outputs = sort_list_elements_alphabetically(outputs)
sorted_signals = sort_list_elements_alphabetically(signals)

def convert(source: str) -> list:
    return [[''.join(sorted(chunk)) for chunk in item.split()] for item in source]

def sortedbylength(arr: list) -> list:
    # Sorting using sorted function
    # providing key as len
    return [ sorted(item, key=len) for item in arr]


print(outputs)
woo = convert(outputs)
print(woo)

print("Sorted by length")
print(sortedbylength(convert(outputs)))

doo = sortedbylength(convert(outputs))
print(find(doo))













"""
This code takes a brute  force  approach. I  should understand it. 
https://github.com/MasterMedo/aoc/blob/master/2021/day/8.py
"""

