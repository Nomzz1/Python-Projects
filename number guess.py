from random import randint
num = randint(0,500)
guess = -1
guesses = 8
while guess != num:
    if guesses == 0:
        break;
    guess = int(input("Guess a number: "))
    if guess > num:
        print("Too high. Try again")
    elif guess < num:
        print("Too low. Try again.")
    guesses -= 1
    print(f"You have {guesses} guesses left.\n")
if guesses == 0:
    print("Sorry, game over. You used all your guesses.")
    print(f"The number was {num}.")
else:
    print("Well done! You guessed the number!")
