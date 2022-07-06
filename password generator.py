print("Welcome to the password generator.")
print("**********************************")
password = ""
print("Do you have any children?")
cc = input()
if cc == "yes":
    print("What is the name of your first child?")
    cn = input().upper()
    password += cn[0]
if cc == "no":
    print("Do you have any pets?")
    pc = input()
    if pc == "yes":
        print("What is the name of your first pet?")
        pn = input().upper()
        password += pn[0]
    if pc == "no":
        print("What is your name?")
        n = input().upper()
        password += n[0]
print("Type in a random word (Must be at least 3 letters long).")
w = input()
password += w[0]
password += w[1]
password += w[2]
print("What is your favourite song?")
s = input()
password += s[0]
password += s[1]
password += s[2]
print("What is your favourite number?")
no = input()
password += no[0]
print("What year were you born?")
bd = input()
password += bd[0]
print("Your perfect password is:",password)