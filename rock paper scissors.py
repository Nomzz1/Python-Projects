import random
print("Welcome to the rock, paper, scissors game.")
print("The game will be a best of three.")
print("The choice picked by the computer is entirely random.")
print("The winner will be picked at the end.")
print("Enjoy!\n")
turns = 0
uscore = 0
cscore = 0
while turns < 3:
  turns += 1
  print("This is game",turns,"out of 3.")
  print("Rock ,Paper, Scissors, SHOOT!")
  uc = input().lower()
  if uc == "r":
    uc = "rock"
  if uc == "s":
    uc = "scissors"
  if uc == "p":
    uc = "paper"
  print("You picked",uc)
  cc = random.choice(["rock","paper","scissors"])
  print("The computer picked",cc)
  if uc == "rock":
    if cc == "rock":
      print("It's a draw!")
    if cc == "paper":
      print("You lose!")
      cscore += 1
    if cc == "scissors":
      print("You win!")
      uscore += 1
  elif uc =="paper":
    if cc == "paper":
      print("It's a draw!")
    if cc == "scissors":
      print("You lose!")
      cscore += 1
    if cc == "rock":
      print("You win!")
      uscore += 1
  elif uc == "scissors":
    if cc == "scissors":
      print("It's a draw!")
    if cc == "rock":
      print("You lose!")
      cscore += 1
    if cc == "paper":
      print("You win!")
      uscore += 1
  else:
    print("You did not enter a valid option, please try again")
  print("\n")
print("Your score was",uscore)
print("The computer's score was",cscore)
if uscore > cscore:
  print("You win!")
elif cscore > uscore:
  print("You lose!")
else:
  print("It's a draw!")
input()
