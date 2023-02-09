def rle(n):
    n = n.split()
    endlist = []
    counter = 0
    for i in range(len(n)):
        counter += 1
        if i+1 >= len(n):
            endlist.append(f"{n[i]} {counter:08b}")
            break
        if n[i+1] != n[i]:
            endlist.append(f"{n[i]} {counter:08b}")
            counter = 0
    string = ""
    for i in endlist:
        string += i + " "
    return string
print(rle(input()))
