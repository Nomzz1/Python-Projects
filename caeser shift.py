def shift(text, n):
    new = ""
    for i in text:
        if 65 <= ord(i) <= 90:
            if ord(i) > 90 - n:
                new += chr(ord(i)+n-26)
            else:
                new += chr(ord(i)+n)
        elif 97 <= ord(i) <= 122:
            if ord(i) > 122 - n:
                new += chr(ord(i)+n-26)
            else:
                new += chr(ord(i)+n)
        else:
            new += i
    return new
while True:
    print(shift(input(),13))
