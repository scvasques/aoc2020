import re

def buildMap(map, outer, innerStr):
	if innerStr == "no other bags.":
		return
	innerList = innerStr.split(", ")
	for i in innerList:
		inner = re.match("^([\w]+ [\w]+)", i[2:]).group()
		if inner in map:
			map[inner].add(outer)
		else:
			map[inner] = {outer}

def findOuterBags(map, color, res):
	if color in map:
		outer = map[color]
		res.update(outer)
		aux = set()
		for i in outer:
			aux.update(findOuterBags(map, i, res))
		res.update(aux)
		return res
	return set()

def main():
	with open("input.txt", "r") as f:
		lines = f.read().splitlines()
	map = {}
	for i in lines:
		outer = re.match("^([\w]+ [\w]+)", i).group()
		buildMap(map, outer, i[len(outer):].replace(" bags contain ", ""))
	res = findOuterBags(map, "shiny gold", set())
	print("Total: " + str(len(res)))
		
main()