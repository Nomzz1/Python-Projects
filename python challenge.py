import random
print("Enter Player 1 name")
rounds = 5
while rounds != 0:
    dice_roll1 = (random.randint(1,6))
    dice_roll2 = (random.randint(1,6))
    dice_roll3 = (random.randint(1,6))
    dice_roll4 = (random.randint(1,6))
    dice_roll5 = (random.randint(1,6))
    dice_roll6 = (random.randint(1,6))
    p1_roll = dice_roll1 + dice_roll2
    if dice_roll1 == dice_roll2:
        p1_roll += dice_roll5
    p2_roll = dice_roll3 + dice_roll4
    if dice_roll3 == dice_roll4:
        p2_roll += dice_roll6
    if p1_roll%2 == 1:
        p1_score = p1_roll-5
    else:
        p1_score = p1_roll+10
    if p2_roll%2 == 1:
        p2_score = p2_roll-5
    else:
        p2_score = p2_roll+10
    if p1_score < 0:
        p1_score = 0
    if p2_score < 0:
        p2_score = 0
    rounds -= 1
if p1_score < p2_score:
    print("Player 1 Wins!")
if p1_score > p2_score:
    print("Player 2 Wins!")
if p1_score == p2_score:
    print("It's a Draw!")