with open("input.txt", "r") as f:
    lines = f.readlines()
lines = [int(s) for s in lines]
for i in lines:
    for j in lines:
        for k in lines:
            if i + j + k == 2020:
                print("i: " + str(i))
                print("j: " + str(j))
                print("k: " + str(k))
                print("i + j + k: " + str(i + j + k))
                print("i * j * k: " + str(i * j * k))
                exit(0)