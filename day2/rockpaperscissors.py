with open('day2/input.txt') as f:
    lines = f.read()
score = 0
for rps in lines.split("\n"):
    match rps:
        case "A X":
            score += 4
        case "A Y":
            score += 8
        case "A Z":
            score += 3
        case "B X":
            score += 1
        case "B Y":
            score += 5
        case "B Z":
            score += 9
        case "C X":
            score += 7
        case "C Y":
            score += 2
        case "C Z":
            score += 6

print("With my strategy guide, my total score would be " + str(score))

newScore = 0
for rps in lines.split("\n"):
    match rps:
        case "A X":
            newScore += 3
        case "A Y":
            newScore += 4
        case "A Z":
            newScore += 8
        case "B X":
            newScore += 1
        case "B Y":
            newScore += 5
        case "B Z":
            newScore += 9
        case "C X":
            newScore += 2
        case "C Y":
            newScore += 6
        case "C Z":
            newScore += 7

print("With my unltra top secret strategy guide, my total score would be " + str(newScore))
