import re

with open('day4/input.txt') as f:
    lines = f.read()

sectionRanges = list(map(lambda x: re.split("[,-]", x), lines.split("\n")))
sum = 0
for rng in sectionRanges:
    if (int(rng[0]) >= int(rng[2]) and int(rng[1]) <= int(rng[3])):
        sum += 1
    elif (int(rng[2]) >= int(rng[0]) and int(rng[3]) <= int(rng[1])):
        sum += 1
print("The sum of assignment pairs where one range fully contains the other is " + str(sum))

sum = 0
for rng in sectionRanges:
    if (int(rng[1]) >= int(rng[2]) and int(rng[0]) < int(rng[3])) or (int(rng[3]) >= int(rng[0]) and int(rng[2]) < int(rng[1])):
        sum += 1
print("The sum of assignment pairs where one range contains the other is " + str(sum))
