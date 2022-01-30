"""
--- Day 10: Syntax Scoring ---

You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

Syntax error in navigation subsystem on line: all of them

All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).

The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

    If a chunk opens with (, it must close with ).
    If a chunk opens with [, it must close with ].
    If a chunk opens with {, it must close with }.
    If a chunk opens with <, it must close with >.

So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]

Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

    {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
    [[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
    [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
    [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
    <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.

Stop at the first incorrect closing character on each corrupted line.

Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.

In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal > was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!

Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?

"""
from collections import deque
from pathlib import Path
from collections import deque

input_data: list[int] = list(Path('day10_input.txt').read_text().rstrip().split('\n'))

Opening_brackets = {'(','[','{','<'}
Closing_brackets = {')',']','}','>'}
ReMatches = {
    '(': ')', '[': ']', '{': '}', '<': '>'
}

Matches = {
    ')': '(', ']': '[', '}': '{', '>': '<'
}
values = {')': 3, ']': 57, '}': 1197, '>': 25137}

# Search a line for the bad characters.
# If an opening bracket is found
# Add its matching closing bracket to a stack
# Get the next bracket, if it is opening bracket add its closing bracket again
# If it is closing bracket then use pop, or popleft during a compare operation
# to remove the last added bracket from the stack.
# If this last added bracket does not match the current bracket, then
# the line is corrupt and increment the total with the value.

"""
We can do this with a deque used as a stack LIFO and a function called.
"""

def getcorruptedchar(line):
    stack = deque()

    #print(stack)
    for bracket in line:
        if bracket in Opening_brackets:
            stack.appendleft(Matches.get(bracket))
            #continue
        elif bracket != stack.popleft():
            #print(values.get(bracket))
            #print(Matches.get(bracket))
            value = values.get(bracket)
            break
    return value



"""
We can do this with a list used as a stack LIFO and a function called.
"""

def getcorruptedchar2(line):
    stack = []
    value = 0
    for bracket in line:
        if bracket in Opening_brackets:
            stack.append(ReMatches.get(bracket))
        elif bracket != stack.pop():
            value = values.get(bracket)
            break
    return value


total = 0
for line in input_data:
  total += getcorruptedchar2(line)

print(total)



"""
We can do this with a deque used as a stack LIFO.
"""

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
values = {')': 3, ']': 57, '}': 1197, '>': 25137}

total = 0
for line in input_data:
    stack = deque()
    for char in line.strip():
        if char == '(' or char == '[' or char == '{' or char == '<':
            stack.appendleft(pairs[char])
        elif stack.popleft() != char:
            total += values[char]
            break
print(total)

"""
We can do this with a list used as a stack LIFO.
"""
total = 0
for line in input_data:
    stack = []
    for char in line:
        if char in Opening_brackets:
            stack.append(pairs[char])
        elif stack.pop() != char:
            total += values[char]
            break
print(total)

"""
--- Part Two ---

Now, discard the corrupted lines. The remaining lines are incomplete.

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

In the example above, there are five incomplete lines:

    [({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
    [(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
    (((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
    {<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
    <{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.

Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

    ): 1 point.
    ]: 2 points.
    }: 3 points.
    >: 4 points.

So, the last completion string above - ])}> - would be scored as follows:

    Start with a total score of 0.
    Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
    Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
    Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
    Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.

The five lines' completion strings have total scores as follows:

    }}]])})] - 288957 total points.
    )}>]}) - 5566 total points.
    }}>}>)))) - 1480781 total points.
    ]]}}]}]}> - 995444 total points.
    ])}> - 294 total points.

Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.

Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?

"""

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
values = {')': 3, ']': 57, '}': 1197, '>': 25137}
total = 0
scores = []

for line in input_data:
    stack = deque()
    for char in line.strip():
        if char == '(' or char == '[' or char == '{' or char == '<':
            stack.appendleft(pairs[char])
        elif stack.popleft() != char:
            total += values[char]
            break
    else:
        # If all characters were read w/o corruption then find score to complete line
        score = 0
        for c in stack:
            score = (score * 5) + ')]}>'.index(c) + 1
        scores.append(score)

print(scores)
print(sorted(scores)[len(scores) // 2])
