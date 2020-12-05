import math

def positionNumber(str, floor, ceil):
    if floor == ceil:
        return floor
    if str[0] in ["F", "L"]:
        return positionNumber(str[1:], floor, math.floor((floor + ceil) / 2))
    return positionNumber(str[1:], math.ceil((floor + ceil) / 2), ceil)

with open("input.txt", "r") as f:
	lines = f.read().splitlines() 
highest = 0
for i in lines:
    row = positionNumber(i[0:-3], 0, pow(2,7) - 1)
    col = positionNumber(i[-3:], 0, pow(2,3) - 1)
    seatId = row * 8 + col
    if highest < seatId:
        highest = seatId
print("Highest seat ID: " + str(highest))