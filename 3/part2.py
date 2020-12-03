import math

def expandTerrain(lines, right):
    mult = math.ceil((len(lines) * (right + 1)) / len(lines[0]))
    t = []
    for i in lines:
        t.append((mult * i[:-1]))
    return t

def countTrees(terrain, right, down):
    count = 0
    x = 0
    y = 0
    while y < len(terrain):
        if terrain[y][x] == "#":
            count += 1
        x += right
        y += down
    return count

with open("input.txt", "r") as f:
	lines = f.readlines()
terrain = expandTerrain(lines, 7)
total = countTrees(terrain, 1, 1)
total *= countTrees(terrain, 3, 1)
total *= countTrees(terrain, 5, 1)
total *= countTrees(terrain, 7, 1)
total *= countTrees(terrain, 1, 2)
print("Total: " + str(total))