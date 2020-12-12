yAxis = {"N": 1, "S": -1}
xAxis = {"E": 1, "W": -1}
facingAxis = {180: "E", 90: "N", 0: "W", 270: "S"}
facingDir = {"L": -1, "R": 1}

def move(pos, cmd):
	val = int(cmd[1:])
	if cmd[0] in xAxis:
		pos["x"] += val * xAxis[cmd[0]]
	elif cmd[0] in yAxis:
		pos["y"] += val * yAxis[cmd[0]]
	elif cmd[0] in facingDir:
		pos["dir"] += val * facingDir[cmd[0]]
		if pos["dir"] < 0:
			pos["dir"] = pos["dir"] + 360
		elif pos["dir"] >= 360:
			pos["dir"] = pos["dir"] - 360
	elif cmd[0] == "F":
		move(pos, facingAxis[pos["dir"]] + cmd[1:])

def main():
	with open("input.txt", "r") as f:
		lines = f.read().splitlines()
	pos = {"x": 0, "y": 0, "dir": 180}
	for i in lines:
		move(pos, i)
	print("Total: " + str(abs(pos["x"]) + abs(pos["y"])))

main()