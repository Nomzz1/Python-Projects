def dmg(x):
    if x <= 20:
            return 70
    elif x >= 40:
            return 21
    return -2.45 * (x - 20) + 70
while True:
    print(dmg(float(input())))