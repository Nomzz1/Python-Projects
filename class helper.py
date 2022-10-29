scores = {}
while True:
    print("Enter the student's name and test score e.g. \"Sarah 26\".")
    print("Enter -1 to end.")
    nameAndScore = input()
    if nameAndScore == "-1":
        break
    split = nameAndScore.split()
    scores.update({split[0]:float(split[1])})
scoreList = list(scores.values())
scoreList = sorted(scoreList)
mean = sum(scoreList)/len(scoreList)
high = [keys for keys, values in scores.items() if values == max(scoreList)][0]
low = [keys for keys, values in scores.items() if values == min(scoreList)][0]
print(f"The average score was {mean}.")
print(f"The highest scoring student was {high} with score {scores[high]}.")
print(f"The lowest scoring student was {low} with score {scores[low]}.")
