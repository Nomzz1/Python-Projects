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
if len(text)%2 == 1:
    text += "Z"
message = []
for i in range(len(text)//2):
    message.append(text[:2])
    text = text[2:]
# Encryption process
newmessage = []
for i in message:
    coords = []
    for j in range(5):
        for k in range(5):
            if table[j][k] == i[0]:
                coords.append((j,k))
    for j in range(5):
        for k in range(5):
            if table[j][k] == i[1]:
                coords.append((j,k))
    # Co-ordinate variables
    c00 = coords[0][0]
    c01 = coords[0][1]
    c10 = coords[1][0]
    c11 = coords[1][1]
    # Same column
    if c00 == c10:
        # Wrapping if too big
        if c00 == 4:
            c00 = -1
        if c10 == 4:
            c10 = -1
        newmessage.append(table[c00][c01+1]+table[c10][c11+1])
    # Same row
    elif c01 == c11:
        # Wrapping if too big
        if c01 == 4:
            c01 = -1
        if c11 == 4:
            c11 = -1
        newmessage.append(table[c00+1][c01]+table[c10+1][c11])
    # Rectangle
    else:
        newmessage.append(table[c00][c11]+table[c10][c01])
finaltext = ""
for i in newmessage:
    finaltext += i
final = ""
for i in range(len(finaltext)):
    if i % 5 == 0:
        final += " "
    final += finaltext[i]
print(f"Your encrypted text is: {final}")
