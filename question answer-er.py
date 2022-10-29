import random
while True:
    print("Welcome to the question answer-er.")
    print("It can only be a yes or no question.")
    print("What is your question?")
    input()
    choice = random.choice(["Yes","No"])
    print(choice)
