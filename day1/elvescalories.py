with open('day1/input.txt') as f:
    lines = f.read()

elvesCalories = list(map(lambda x: x.split("\n"), lines.split("\n\n")))

elvesCaloriesInt = list(
    map(lambda x: list(
        map(lambda y: int(y), x)), elvesCalories))

elvesCaloriesSum = list(map(lambda x: sum(x), elvesCaloriesInt))

elvesCaloriesMax = max(elvesCaloriesSum)

print("The elf who carries the most calories carries " +
      str(elvesCaloriesMax) + " calories")

elvesCaloriesSum.sort()
elvesCaloriesSum.reverse()

print("The three elves who carries the most calories carries a total of " +
      str(elvesCaloriesSum[0] + elvesCaloriesSum[1] + elvesCaloriesSum[2]) + " calories")
