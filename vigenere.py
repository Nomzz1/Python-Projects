from math import ceil
text = input("Enter your text to encrypt: ").upper().replace(" ","")
key = input("Enter your key: ").upper().replace(" ","")
key = key * ceil(len(text)/len(key))
finaltext = ""
for i in range(len(text)):
    letter = ord(text[i]) - 65
    shift = ord(key[i]) - 65
    final = ((letter + shift) % 26) + 65
    finaltext += chr(final)
encrypted = ""
for i in range(len(finaltext)):
    if i % 5 == 0:
        encrypted += " "
    encrypted += finaltext[i]
print(f"Your encrypted text is: {encrypted}")
