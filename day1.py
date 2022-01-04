# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def countincreases(val):
    # compare two lines and increment the counter if the next line
    # is greater than the last line.
    print(f"The number of increases between 2 consecutive elements: { sum(a < b for a, b in zip(val, val[1:])) }")

    #  grab three elements from the list
    tri = [sum(trio) for trio in zip(val, val[1:], val[2:])]
    print(f"The increases in sliding window of three elements:  { sum(a < b for a, b in zip(tri, tri[1:])) } ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = [int(x) for x in open('day1_input.txt', 'r')]
    countincreases(file)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
