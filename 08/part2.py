import operator
ops = { "+": operator.add, "-": operator.sub }

def switchCmd(line):
	cmd = line.split(" ")[0]
	return line.replace("nop", "jmp") if cmd == "nop" else line.replace("jmp", "nop")

def execute(lines):
	acc = 0
	i = 0
	executed = []
	while i < len(lines):
		cmd = lines[i].split(" ")
		if i in executed:
			return -1
		executed.append(i)
		if cmd[0] == "acc":
			acc = ops[cmd[1][0]](acc, int(cmd[1][1:]))
			i += 1
		elif cmd[0] == "jmp":
			i = ops[cmd[1][0]](i, int(cmd[1][1:]))
		else:
			i += 1
	return acc

def main():
	with open("input.txt", "r") as f:
		lines = f.read().splitlines()
	switchable = [i for i, elem in enumerate(lines) if lines[i].split(" ")[0] in ("jmp", "nop")]
	for i in switchable:
		lines[i] = switchCmd(lines[i])
		res = execute(lines)
		if res >= 0:
			print("Accumulator: " + str(res))
			exit(0)
		lines[i] = switchCmd(lines[i])

main()