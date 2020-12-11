def validLine(line):
	split = line.split(": ")
	rules = split[0]
	password = split[1]
	splitRules = rules.split(" ", 1)
	splitNum = splitRules[0].split("-")
	p1 = int(splitNum[0])
	p2 = int(splitNum[1])
	letter = splitRules[1]
	return (password[p1-1] == letter) != (password[p2-1] == letter)

with open("input.txt", "r") as f:
	lines = f.readlines()
count = 0
for i in lines:
	if validLine(i):
		count += 1
print("Number of valid lines: " + str(count))