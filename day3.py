from collections import Counter
print("Advent of Code 2021 - Day 3")


def get_input():
    data = []
    with open("day3_input.txt") as f:
        data = f.readlines()
    return data

def solve(data):
    gamma, epsilon = "", ""
    bitlength = (len(data[0])-1)
    for i in range(bitlength):
        bits: object
        foo = len(data)//2
        doo = sum(bits[i] == "1" for bits in data )
        if doo > foo:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)

def solve2():
    data =  get_input()
    i = 0
    while len(data) >1:
        val = ""
        c = Counter([bits[i] for bits in data ])
        val = "1" if c["1"] >= c["0"] else "0"
        data = [bits for bits in data if bits[i] == val ]
        i += 1
    oxy = data[0]
    data = get_input()
    i = 0
    while len(data) > 1:
        val = ""
        c = Counter( [bits[i] for bits in data])
        val = "0" if c["0"] <= c["1"] else "1"
        data = [bits for bits in data if bits[i] == val ]
        i += 1
    co2 = data[0]
    return int(oxy,2) * int(co2,2)

print(solve2())
#print(solve2(get_input()))