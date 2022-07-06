def cap(x, y):
    z = ""
    count = 0
    for i in x:
        if count == y:
            i = i.upper()
        z += i
        count += 1
    return z