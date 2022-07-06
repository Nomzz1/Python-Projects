def find_longest(s):
    s = s.replace("!","")
    s = s.replace(",","")
    s = s.replace("\"", "")
    s = s.replace(".","")
    s = s.lower()
    s = s.split()
    s = sorted(s, key = len, reverse = True)
    return s[0]