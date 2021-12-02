def solveA(file):
    h, d = 0, 0
    for line in file:
        action, value = line.split(" ")
        value = int(value)
        if action[0] == 'f':
            h += value
        elif action[0] == 'd':
            d += value
        else:
            d -= value
    return h * d


def solveB(file):
    h, d, a = 0, 0, 0
    for line in file:
        action, value = line.split(" ")
        value = int(value)
        if action[0] == 'd':
            a += value
        elif action[0] == 'u':
            a -= value
        else:
            h += value
            d += a * value
    return h * d


file = open("aoc_input", "r")
print(solveB(file))
