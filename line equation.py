print("Enter the two co-ordinates of a line to find its equation.")
c1x = int(input("First x co-ordinate:"))
c1y = int(input("First y co-ordinate:"))
c2x = int(input("Second x co-ordinate:"))
c2y = int(input("Second y co-ordinate:"))
if c1x < c2x:
    m = (c2y - c1y)/(c2x - c1x)
    c = c2y - (m*c2x)
    if m == 1:
        lineq = "y = x +"+str(c)
    else:
        lineq = "y = "+str(m)+"x + "+str(c)
elif c2x < c1x:
    m = (c1y - c2y)/(c1x - c2x)
    c = c1y - (m*c1x)
    if m == 1:
        lineq = "y = x +"+str(c)
    else:
        lineq = "y = "+str(m)+"x + "+str(c)
elif c1x == c2x:
    lineq = "x = "+str(c1x)
elif c1y == c2y:
    lineq = "y = "+str(c1y)
else:
    lineq = "Error occured"
print("The equation for your line is:",lineq)
