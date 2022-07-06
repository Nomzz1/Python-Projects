MULTIPLIER = 1000
print("Enter the length of the pool in metres")
l = int(input())
print("Enter the width of the pool in metres")
w = int(input())
print("Enter the depth of the pool in metres")
d = int(input())
vol = l*w*d
litres = vol*MULTIPLIER
print("The total capacity of the pool is",litres,"litres")
input()
