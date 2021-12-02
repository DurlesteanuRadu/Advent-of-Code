def solveA(file):
    sol = 0
    prev = int(file.readline())
    for line in file:
        cur = int(line)
        if prev < cur:
            sol += 1
        prev = cur
    return sol


def solveB(file):
    sol = 0
    prev3 = [int(file.readline()), int(file.readline()), int(file.readline())]
    for line in file:
        cur = int(line)
        if sum(prev3) < sum(prev3) - prev3[0] + cur:
            sol += 1
        prev3 = [prev3[1], prev3[2], cur]
    return sol


file = open("aoc_input", "r")
print(solveB(file))
