def validLine(line):
	split = line.split(": ")
	rules = split[0]
	password = split[1]
	splitRules = rules.split(" ", 1)
	splitNum = splitRules[0].split("-")
	min = int(splitNum[0])
	max = int(splitNum[1])
	letter = splitRules[1]
	total = password.count(letter)
	return max >= total and min <= total

with open("input.txt", "r") as f:
	lines = f.readlines()
count = 0
for i in lines:
	if validLine(i):
		count += 1
print("Number of valid lines: " + str(count))