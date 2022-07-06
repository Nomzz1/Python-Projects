speed = int(input("Speed (mph): "))
if speed > 70:
    print("Issue Fine")
    dif = speed - 70
    print("The driver is",dif,"mph over the speed limit.")
else:
    print("No Action.")
    if speed == 70:
        print("The driver is at the speed limit.")
    else:
        dif = 70 - speed
        print("The driver is",dif,"mph under the speed limit.")
input()
