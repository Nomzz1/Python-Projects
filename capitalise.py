def cap(x, y):
    z = ""
    count = 0
    for i in x:
        if count == y:
            i = i.upper()
        z += i
        count += 1
    return z

def mock(word):
    string = ""
    count = 0
    for i in word:
        if count % 2 == 0:
            string += i.upper()
        else:
            string += i.lower()
        count += 1
    return string
            
