from math import sqrt, tan, degrees
alpha = 36.875

def calculateRadius(n): # find radius of mountain
    return (n/tan(degrees(alpha)))

def calculateDistance(n1,n2): # formula for distance between two points
    return sqrt(((n1[0]-n2[0])**2)+((n1[1]-n2[1])**2))

def isIntersect(r1,r2,d):
    return (r1 + r2 - d)

pointList = [(0,28,0),(1,27,0.375),(2,27,0.1875),(3,25,1.3125),(3,26,1.3125),(7,26,0.5625),(6,23,2.4375),(5,22,2.8125),(7,19,3.375),(7,18,3.5625),(5,15,4.125),(6,13,4.3125),(9,13,4.125),(11,17,3.375),(11,18,3.1875),(9,22,2.4375),(10,25,0.5625),(13,22,1.6875),(13,23,1.125),(14,23,0.5625),(15,22,0.9375),(17,21,0.375),(18,19,1.3125),(17,18,2.0625),(18,17,2.0625),(19,18,1.3125),(21,17,0.375),(22,15,0.9375),(23,14,0.5625),(23,13,1.125),(22,13,1.6875),(18,11,3.1875),(17,11,3.375),(13,9,4.125),(13,6,4.3125),(15,5,4.125),(18,7,3.5625),(19,7,3.375),(22,5,2.8125),(23,6,2.4375),(22,9,2.4375),(25,10,0.5625),(26,7,0.5625),(26,3,1.3125),(27,1,0.375),(27,2,0.1875),(25,3,1.3125),(23,3,2.625),(21,2,3.1875),(17,2,3.9375),(14,3,4.3125),(10,3,4.6875),(7,3,4.875),(2,1,5.0625),(1,2,5.0625),(3,7,4.875),(3,10,4.6875),(3,14,4.3125),(2,17,3.9375),(2,21,3.1875),(3,23,2.625)]
distances = []
for i in range(len(pointList)):
    p1 = pointList[i]
    try:
        p2 = pointList[i+1]
    except IndexError:
        p2 = (0,28,0)
    r1 = calculateRadius(p1[2])
    r2 = calculateRadius(p2[2])
    d = calculateDistance(p1,p2)
    if isIntersect(r1,r2,d) < 0:
        distances.append((r1,(d - r1 - r2),r2))
    elif isIntersect(r1,r2,d) == 0:
        distances.append((r1,0,r2))
    elif isIntersect(r1,r2,d) > 0:
        x = (r1 - r2 + d)/2
        y = d - x
        distances.append((x,0,y))
distances2 = []
for i in distances:
    x = i[0]
    y = i[1]
    z = i[2]
    if x < 0:
        x *= -1
    if y < 0:
        y *= -1
    if z < 0:
        z *= -1
    distances2.append((x,y,z))
totalTime = 0
for i in distances2:
    x = i[0]
    y = i[1]
    z = i[2]
    x /= 0.004
    y /= 0.002
    z /= 0.001
    totalTime += x + y + z
print(totalTime)
