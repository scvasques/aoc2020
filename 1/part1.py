with open("input.txt", "r") as f:
    lines = f.readlines()
lines = [int(s) for s in lines]
for i in lines:
    for j in lines:
		if i + j == 2020:
			print("i: " + str(i))
			print("j: " + str(j))
			print("i + j: " + str(i + j))
			print("i * j: " + str(i * j))
			exit(0)