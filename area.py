length = float(input("What is the length of your rectangle? "))
width = float(input("What is the width of your rectangle? "))
area = length * width
if length == width:
    print(f"This is a square of area {area:.2f}")
else:
    print(f"This is a rectangle of area {area:.2f}")
