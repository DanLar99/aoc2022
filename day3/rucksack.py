with open('day3/input.txt') as f:
    lines = f.read()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = {}
for i in range(0, len(alphabet)):
    priority[alphabet[i]] = i + 1

rucksacks = list(
    map(lambda x: [x[:int(len(x)/2)], x[int(len(x)/2):]], lines.split("\n")))

prioritySum = 0
for compartements in rucksacks:
    compOne = list(dict.fromkeys(compartements[0]))
    for item in compOne:
        if compartements[1].count(item) > 0:
            prioritySum += priority[item]

print("The sum of priorities of items in both compartments of each rucksack is " + str(prioritySum))

rucksacks = lines.split("\n")
prioritySum = 0

for i in range(0, len(rucksacks), 3):
    sackOne = list(dict.fromkeys(rucksacks[i]))
    for item in sackOne:
        if rucksacks[i+1].count(item) > 0 and rucksacks[i+2].count(item) > 0:
            prioritySum += priority[item]

print("The sum of priorities of badges in all three rucksacks of each group is " + str(prioritySum))
