"""
target area: x=253..280, y=-73..-46

Test
target area: x=20..30, y=-10..-5
EXPECTED = 45
"""

from pathlib import Path


def main() -> int:

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

    y0 = abs(target[1][0]) -1
    ans = y0 * y0 - (y0 - 1) * y0 // 2
    print(ans)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())