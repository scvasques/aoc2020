import operator
ops = { "+": operator.add, "-": operator.sub }

def main():
	with open("input.txt", "r") as f:
		lines = f.read().splitlines()
	acc = 0
	i = 0
	executed = []
	while i < len(lines):
		cmd = lines[i].split(" ")
		if i in executed:
			print("Accumulator: " + str(acc))
			exit(0)
		executed.append(i)
		if cmd[0] == "acc":
			acc = ops[cmd[1][0]](acc, int(cmd[1][1:]))
			i += 1
		elif cmd[0] == "jmp":
			i = ops[cmd[1][0]](i, int(cmd[1][1:]))
		else:
			i += 1

main()