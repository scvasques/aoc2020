def seatsInDir(lines, y, yIncr, x, xIncr):
	res = []
	y += yIncr
	x += xIncr
	while y >= 0 and y < len(lines) and x >= 0 and x < len(lines[0]):
		res.append(lines[y][x])
		if lines[y][x] in ["#","L"]:
			break
		y += yIncr
		x += xIncr
	return res

def adjacentSeats(lines, i, j):
	res = []
	for pos in {(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)}:
		res += seatsInDir(lines, i, pos[0], j, pos[1])
	return res

def nextRound(lines):
	new = []
	for i in range(len(lines)):
		line = ""
		for j in range(len(lines[i])):
			if (lines[i][j] == "L" and adjacentSeats(lines, i, j).count("#") == 0) or (lines[i][j] == "#" and adjacentSeats(lines, i, j).count("#") >= 5):
				line += "L" if lines[i][j] == "#" else "#"
			else:
				line += lines[i][j]
		new.append(line)
	return new

def main():
	with open("input.txt", "r") as f:
		lines = f.read().splitlines()
	lastRound = lines
	while True:
		round = nextRound(lastRound)
		if lastRound == round:
			break
		lastRound = round
	print("Total: " + str(sum([s.count("#") for s in lastRound])))

main()