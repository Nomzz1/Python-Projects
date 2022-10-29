# Import ceil function
from math import ceil
# Take inputs
key = input("Enter your key: ").upper().replace(" ","").replace("J","I")
text = input("Enter your text to encrypt: ").upper().replace(" ","")
# Create table
key = list(key)
letters = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")
combined = []
for i in key:
    if i in combined:
        pass
    else:
        combined.append(i)
for i in letters:
    if i in combined:
        pass
    else:
        combined.append(i)
table = []
for i in range(5):
    table.append(combined[:5])
    combined = combined[5:]
# Format text (separating doubles)
newtext = ""
for i in range(len(text)):
    newtext += text[i]
    try:
        if text[i] == text[i+1]:
            newtext += "X"
    except IndexError:
        pass
text = newtext
# Format text (blocks of 2 letters)
message = []
for i in range(ceil(len(text)/2)):
    message.append(text[:2])
    text = text[2:]
for i in table:
    print(i)
print(message)
