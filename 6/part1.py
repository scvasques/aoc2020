with open("input.txt", "r") as f:
	lines = f.read().replace('\n\n', ',').replace("\n", "")
groups = lines.split(",")
count = 0
for i in groups:
	count += len(set(i))
print("Sum of counts: " + str(count))