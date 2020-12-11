import re

class Space:
	def __init__(self, name, qty):
		self.name = name
		self.qty = qty
	def __hash__(self):
		return hash((self.name, self.qty))
	def __eq__(self, other):
		if not isinstance(other, type(self)): return NotImplemented
		return self.name == other.name and self.qty == other.qty
	def __repr__(self):
		return "{'" + self.name + "', " + str(self.qty) + "}"

def buildMap(map, outer, innerStr):
	if innerStr == "no other bags.":
		map[outer] = {}
		return
	innerList = innerStr.split(", ")
	for i in innerList:
		inner = re.match("^([\w]+ [\w]+)", i[2:]).group()
		space = Space(inner, int(i[:1]))
		if outer in map:
			map[outer].add(space)
		else:
			map[outer] = {space}

def countInnerBags(map, color):
	if color in map:
		innerSpaces = map[color]
		count = 0
		for i in innerSpaces:
			count += i.qty + i.qty * countInnerBags(map, i.name)
		return count
	return 0

def main():
	with open("input.txt", "r") as f:
		lines = f.read().splitlines()
	map = {}
	for i in lines:
		outer = re.match("^([\w]+ [\w]+)", i).group()
		buildMap(map, outer, i[len(outer):].replace(" bags contain ", ""))
	res = countInnerBags(map, "shiny gold")
	print("Total: " + str(res))
		
main()