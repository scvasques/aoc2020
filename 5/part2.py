import math

def positionNumber(str, floor, ceil):
    if floor == ceil:
        return floor
    if str[0] in ["F", "L"]:
        return positionNumber(str[1:], floor, math.floor((floor + ceil) / 2))
    return positionNumber(str[1:], math.ceil((floor + ceil) / 2), ceil)

with open("input.txt", "r") as f:
	lines = f.read().splitlines() 
seatIds = []
for i in lines:
    row = positionNumber(i[0:-3], 0, pow(2,7) - 1)
    col = positionNumber(i[-3:], 0, pow(2,3) - 1)
    seatIds.append(row * 8 + col)
seatIds.sort()
prev = seatIds[0]
for i in seatIds:
    if i - prev == 2:
        print("missing: " + str(i - 1))
        exit(0)
    prev = i