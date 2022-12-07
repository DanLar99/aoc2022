with open('day6/input.txt') as f:
    line = f.read()

for i in range(len(line) - 4 + 1):
    if len(dict.fromkeys(line[i: i + 4])) == 4:
        print("The amount of characters needed to be processed before the first start-of-packet marker is detected is " + str(i + 4))
        break

for i in range(len(line) - 14 + 1):
    if len(dict.fromkeys(line[i: i + 14])) == 14:
        print("The amount of characters needed to be processed before the first start-of-message marker is detected is " + str(i + 14))
        break
