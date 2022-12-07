from collections import defaultdict

with open('day7/input.txt') as f:
    lines = f.read().split("\n")

dirStack = []


def def_value():
    return 0


dirDic = defaultdict(def_value)

for line in lines:
    if line == '$ cd /':
        dirStack = ['/']
    elif line == '$ cd ..':
        dirStack.pop()
    elif line[0:4] == '$ cd':
        if len(dirStack) == 0:
            dirStack.append(line[5:])
        else:
            dirStack.append(dirStack[-1] + line[5:])
    elif line == '$ ls':
        continue
    elif line.split()[0].isdigit():
        for dir in dirStack:
            dirDic[dir] += int(line.split()[0])

sum = 0
sortedVals = list(dirDic.values())
sortedVals.sort()
spaceNeeded = 30000000 - (70000000 - sortedVals[-1])
found = False
for val in sortedVals:
    if val <= 100000:
        sum += val
    if val >= spaceNeeded:
        if not found:
            print('The total size of the deleted directory is ' + str(val))
        found = True

print('The sum of the total sizes of the directories is ' + str(sum))
