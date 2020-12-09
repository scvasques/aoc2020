def valid(number, preamble):
	for i in preamble:
		for j in preamble:
			if i != j and i + j == number:
				return True
	return False

def main():
	with open("input.txt", "r") as f:
		lines = f.read().splitlines()
	numbers = [int(i) for i in lines]
	preambleSize = 25
	for i in range(preambleSize, len(numbers)):
		if not valid(numbers[i], numbers[i-preambleSize:i]):
			print("Invalid number:" + str(numbers[i]))
			exit(0)

main()