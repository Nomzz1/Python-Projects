def looksay(n):
    string = ""
    counter = 0
    for i in range(len(n)):
        counter += 1
        if i+1 >= len(n):
            string += str(counter) + n[i]
            return string
        if n[i+1] != n[i]:
            string += str(counter) + n[i]
            counter = 0
        else:
            pass
global count
count = 0
def recurse(n):
    global count
    count += 1
    print(looksay(n))
    if count < 8:
        recurse(looksay(n))
recurse("1")
