p1t = 80
p2t = 60
et = p1t + p2t
p1s = int(input())
p2s = int(input())
es = p1s + p2s
ep = "true"
if (p1s/p1t) < 0.40:
    ep = "false"
elif (p2s/p2t) < 0.40:
    ep = "false"
elif (es/et) < 0.50:
    ep = "false"
if ep == "true":
    print("pass")
else:
    print("fail")
