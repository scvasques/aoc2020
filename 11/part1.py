def adjacentSeats(lines, i, j):
	res = []
	for y in range(i-1 if i-1 >= 0 else 0, i+2 if i+2 < len(lines) else len(lines)):
		for x in range(j-1 if j-1 >= 0 else 0, j+2 if j+2 < len(lines[i]) else len(lines[i])):
			if y != i or x != j:
				res.append(lines[y][x])
	return res

def nextRound(lines):
	new = []
	for i in range(len(lines)):
		line = ""
		for j in range(len(lines[i])):
			if (lines[i][j] == "L" and adjacentSeats(lines, i, j).count("#") == 0) or (lines[i][j] == "#" and adjacentSeats(lines, i, j).count("#") >= 4):
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