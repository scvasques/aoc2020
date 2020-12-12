import math

yAxis = {"N": 1, "S": -1}
xAxis = {"E": 1, "W": -1}
facingDir = {"L": -1, "R": 1}

def moveWaypoint(waypoint, dir, val):
	if dir in xAxis:
		waypoint["x"] += val * xAxis[dir]
	elif dir in yAxis:
		waypoint["y"] += val * yAxis[dir]
		
def rotateWaypoint(waypoint, angle):
	x = waypoint["x"]
	y = waypoint["y"]
	cosA = int(math.cos(math.radians(angle)))
	sinA = int(math.sin(math.radians(angle)))
	waypoint["x"] = x * cosA + y * sinA
	waypoint["y"] = -x * sinA + y * cosA

def moveShip(pos, waypoint, val):
	pos["x"] += waypoint["x"] * val
	pos["y"] += waypoint["y"] * val

def main():
	with open("input.txt", "r") as f:
		lines = f.read().splitlines()
	pos = {"x": 0, "y": 0}
	waypoint = {"x": 10, "y": 1}
	for i in lines:
		val = int(i[1:])
		if i[0] in ["N","S","E","W"]:
			moveWaypoint(waypoint, i[0], val)
		elif i[0] in facingDir:
			rotateWaypoint(waypoint, val * facingDir[i[0]])
		elif i[0] == "F":
			moveShip(pos, waypoint, val)
	print("Total: " + str(abs(pos["x"]) + abs(pos["y"])))

main()