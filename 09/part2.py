def valid(number, preamble):
	for i in preamble:
		for j in preamble:
			if i != j and i + j == number:
				return True
	return False

def findSet(nIdx, numbers):
	for i in range(1, len(numbers)-1):
		for begin in range(len(numbers)):
			end = begin + i
			if not begin < nIdx < end:
				if numbers[nIdx] == sum(numbers[begin:end+1]):
					return numbers[begin:end+1]

def main():
	with open("input.txt", "r") as f:
		lines = f.read().splitlines()
	numbers = [int(i) for i in lines]
	preambleSize = 25
	for i in range(preambleSize, len(numbers)):
		if not valid(numbers[i], numbers[i-preambleSize:i]):
			res = sorted(findSet(i, numbers))
			print("Weakness: " + str(res[0] + res[len(res)-1]))
			exit(0)

main()