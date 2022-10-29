name = input("What is your name? ")
tests = int(input("How many test scores would you like to enter? "))
scores = []
for i in range(tests):
    score = float(input("Enter your test score: "))
    scores.append(score)
mean = sum(scores)/len(scores)
print(f"The average score is {mean}.")
scores = sorted(scores)
print(f"The top 3 scores are: {scores[-3:]}.")
print(f"The bottom 3 scores are: {scores[:3]}.")
