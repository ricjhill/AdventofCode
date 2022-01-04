
if __name__ == '__main__':

    print("Advent of Code 2021 - Day 2")

    with open("day2_input.txt") as fh:
        lines = fh.readlines()

    m = [a.strip().split() for a in lines]
 #   print(dir(m))
 #   print(type(m))
 #   print(m)

    depth = 0
    aim = 0
    x_axis = 0
    y_axis = 0


# 1568138742
# 1569566610

    for line in m:
        match line[0]:
          case "forward":
            x_axis += int(line[1])
            y_axis += aim * int(line[1])
          case "up":
            #y_axis -= int(line[1])
#            print(y_axis)
            aim -= int(line[1])
          case "down":
            #y_axis += int(line[1])
#            print(y_axis)
            aim += int(line[1])

    final_position = y_axis * x_axis
    print(final_position)
 #   print(aim)
 #   print(aim * final_position)