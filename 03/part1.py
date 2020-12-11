import math

def expandTerrain(lines):
    mult = math.ceil((len(lines) * 4) / len(lines[0]))
    t = []
    for i in lines:
        t.append((mult * i[:-1]))
    return t

with open("input.txt", "r") as f:
	lines = f.readlines()  
terrain = expandTerrain(lines)
count = 0
increment = 3
pos = 0
for i in terrain:
    if i[pos] == "#":
        count += 1
    pos += increment
print("Tree count: " + str(count))