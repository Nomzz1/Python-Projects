import time
pocketmoney =  0.01
totalmoney = 0
for week in range(1,27):
    print("\nIt is week",str(week)+".")
    print("You will get £"+str(pocketmoney))
    pocketmoney += pocketmoney
    totalmoney += pocketmoney
    time.sleep(1)
print("Over 26 weeks you have accumulated £"+format(totalmoney, ".2f")+" of pocket money.")
input("\nPress ENTER to exit program.")
