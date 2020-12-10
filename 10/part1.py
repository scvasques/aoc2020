def main():
	with open("input.txt", "r") as f:
		lines = f.read().splitlines()
	numbers = sorted([int(i) for i in lines])
	numbers.insert(0, 0)
	jolt1 = 0
	jolt3 = 1
	for i in range(len(numbers)-1):
		if numbers[i+1] - numbers[i] == 1:
			jolt1 += 1
		elif numbers[i+1] - numbers[i] == 3:
			jolt3 += 1
	print(jolt1)
	print(jolt3)
	print("Total: " + str(jolt1 * jolt3))

main()