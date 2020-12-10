def possibleCombinations(numbers):
    paths = [1] + [0] * (len(numbers) - 1)
    for i, n in enumerate(numbers):
        for j in range(i - 3, i):
            if(n - numbers[j] <= 3):
                paths[i] += paths[j]
    return paths[-1]

def main():
	with open("input.txt", "r") as f:
		lines = sorted(list(map(int, f.read().splitlines())))
	lines.insert(0, 0)
	total = possibleCombinations(lines)
	print("Total: " + str(total))

main()