print("Welcome to the Secret Society of Secrecy.")
print("To enter you must guess the password.")
print("The password is a number.")
print("Once you type in the correct password you will be let in.")
print("You have 3 Clues. For your first clue type 'clue 1', for your second clue type 'clue 2' , and so on.")
password = input("Guess: ")
while password != "36":
    if password == "clue 1":
        print("Clue: It is a 2 digit number.")
    if password == "clue 2":
        print("Clue: It is a multiple of 3.")
    if password == "clue 3":
        print("Clue: It is a square number.")
    password = input("Wrong. Guess again: ")
if password == "36":
    print("Well done! You are now part of the Secret Society of Secrecy!")
input()
