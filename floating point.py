print("Float to Denary Converter")
print("*************************\n")
def conv(n):
    base = 0
    for i in n:
        base = base*2 + int(i)
    return base
print("Note: Your floating point binary number must be normalised.")
man = input("Enter your mantissa: ")
exp = input("Enter your exponent: ")
shift = len(man) - 1
man = list(man)
man[0] = "-" + man[0]
exp = list(exp)
exp[0] = "-" + exp[0]
final = conv(man) * (2**(conv(exp)-shift))
print(f"Your denary value is {final}")
