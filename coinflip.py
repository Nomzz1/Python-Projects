import random as r
rep = ""
while rep == "":
    rep = input()
    coin = r.randint(0,1)
    if coin == 1:
        print("Heads wins.")
    else:
        print("Tails wins.")
