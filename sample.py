lines = [[direction, int(number)] for direction, number in [
    line.split(" ") for line in open("day2_input.txt", "r+").readlines()]]


def solve(lines, part=1):
    aim = 0
    horiz = 0
    depth = 0
    for line in lines:
        match line:
            case ["forward", number]:
                if part == 1:
                    horiz += number
                else:
                    horiz += number
                    depth = depth + (aim * number)
            case ["up", number]:
                if part == 1:
                    depth -= number
                else:
                    aim -= number
            case ["down", number]:
                if part == 1:
                    depth += number
                else:
                    aim += number
    return horiz * depth


# Print the answers.
print(f"DAY TWO\nPart one: {solve(lines, 1)}\nPart two: {solve(lines, 2)}")