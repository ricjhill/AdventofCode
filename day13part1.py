"""
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.
Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:
Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0
fold along y=7
fold along x=5
The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:
...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):
...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:
#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.
Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.
Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.
The second fold instruction is fold along x=5, which indicates this line:
#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:
#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!
The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.
How many dots are visible after completing just the first fold instruction on your transparent paper?
"""

from pathlib import Path


input_data: list[int] = list(Path('day13_input.txt').read_text().rstrip().split('\n'))
dots = set()


def iscoordinate(line: str) -> int:
    """Returns the x,y coordinates as int if "line" is 2 int castible strings seperated by  a comma
    Parameters
    ----------
    line: str
          a single line from the input file

    Returns
    -------
    int, int:
         two ints describing the x,y coordinates of a mark on the paper

    """
    try:
        x, y = map(int,line.split(','))
        return x, y
    except ValueError:
        return False
    else:
        return False


def isafold(line: str) -> int:
    """Gets the fold x,y coordinates if the line contains 'fold along' string
    Parameters
    ----------
    line: str
          a single line from the input file

    Returns
    -------
    int, int:
         two ints describing the x,y coordinates of a fold


    """
    try:
        if 'fold along' in line:
            f = parsefold(line)
            return f
        else:
            return False
    except Exception:
        False


def parsefold(line: str) -> int:
    """ Returns the fold x,y coordinates

    Parameters
    ----------
    line: str
          a single line from the input file

    Returns
    -------
    int, int:
         two ints describing the x,y coordinates of a fold
    """
    foldx = line[len("fold along "):]
    if foldx[0] == "y":
        return int(0), int(foldx[2:])
    else:
        return int(foldx[2:]), int(0)


def reflect(point: tuple , line: tuple) -> tuple:
    """ Calculates the position of dots  after folding the paper

    :param point: x,y position of a dot/marking
    :param line:  x or y coordinates where line of folding is.
    :return: A tuple containing  the x,y position of a dot after the paper is folded.
    """
    if line[0] != 0:
        return (2*line[0] - point[0], point[1])
    return (point[0], 2*line[1] - point[1])



folds = list(map(isafold, filter(isafold, input_data) ))

coordinates = set(map(iscoordinate, filter(iscoordinate,input_data)  ))


new_dots = set()
fold = folds[0]

for dot in coordinates:
    if fold[0] != 0:
#        # Vertical fold
        if dot[0] > fold[0]:
            new_dots.add(reflect(dot, fold))
        else:
            new_dots.add(dot)
#
    else:
#         # Horizontal fold
        if dot[1] > fold[1]:
            new_dots.add(reflect(dot, fold))
        else:
            new_dots.add(dot)




print('The filtered folds are:')
for s in folds:
    print(s)


print('The filtered coordinates are:')
for x in coordinates:
    print(x)


print('The number of dots visible after completing just the first fold instruction filtered coordinates is:')
ans = len(new_dots)
print(ans)