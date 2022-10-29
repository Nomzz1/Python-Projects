def looksay(n):
    n = str(n)
    final = ""
    counter = 1
    for i in range(len(n)):
        current = n[i]
        try:
            if n[i+1] == current:
                counter += 1
            else:
                final += str(counter) + current
        except IndexError:
            final += str(counter) + current
        return final
print(looksay(12))
