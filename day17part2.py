"""
target area: x=253..280, y=-73..-46
"""

from pathlib import Path

input_data: str = Path('day17_input.txt').read_text().rstrip()
data = input_data[len("target area: x="):].split(', y=')


x_range = (
    # use array slice and  indexing to split  a string.
    int(data[0][:data[0].index("..")]),
    int(data[0][data[0].index("..") + 2:])
)

y_range = (
    int(data[1][:data[1].index("..")]),
    int(data[1][data[1].index("..")+2:])
)

target = (x_range, y_range)
print(target)

# This is the limit of the y velocity
max_yv = abs(target[1][0])
print(max_yv)



def iterate(pos, vel):
    """
    :param pos:  list: current position of shot in x,y
    :param vel:  List: current velocity of shot in x,y
    :return: new position and velocity as lists

    """
    new_pos = [0, 0]
    new_vel = [0, 0]

    new_pos[0] = pos[0] + vel[0]
    new_pos[1] = pos[1] + vel[1]

    new_vel[1] = vel[1] - 1
    if vel[0] > 0:
        new_vel[0] = vel[0] - 1
    if vel[0] < 0:
        new_vel[0] = vel[0] + 1

    return new_pos, new_vel


def is_within(pos, tar):
    """

    :param pos: list: position of the shot [ x_pos, y_pos ]
    :param target: nested tuple (x_min, x_max) ,(y_min, y_max))
    :return:
    """
    return (
            tar[0][0] <= pos[0] <= tar[0][1]\
            and (tar[1][0] <= pos[1] <= tar[1][1])
            )


def is_past(pos, vel, target):
    """
    Calculates if the shot has passed the target. Returns True when passed.

    :param pos: tuple
    :param vel: tuple
    :param target: nested tuple (x_min, x_max) ,(y_min, y_max))
    :return:
    """
    if vel[0] > 0 and pos[0] > target[0][1]:
        return True
    if vel[0] < 0 and pos[0] < target[0][0]:
        return True
    if vel[1] < 0 and pos[1] < target[1][0]:
        return True
    return False


def does_hit(vel, target):
    """
    :param target: tuple  [x_range, y_range]
    """
    pos = (0, 0)
    max_y = 0
    while not is_past(pos, vel, target):
        max_y = max(max_y, pos[1])
        if is_within(pos, target):
            return True, max_y
        pos, vel = iterate(pos, vel)

    return False, None



# Test out a bunch of stuff
ans = 0
y0 = abs(target[1][0]) -1
ans = y0 * y0 - (y0 - 1) * y0 // 2
print(ans)
