with open("input.txt", "r") as f:
	lines = f.read().replace('\n\n', ',')
groups = lines.split(",")
count = 0
for i in groups:
	persons = [set(p) for p in filter(None, i.split("\n"))]
	count += len(set.intersection(*persons))
print("Sum of counts: " + str(count))