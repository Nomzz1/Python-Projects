from math import sqrt, pi, acos, radians
chordLength = sqrt((sqrt(2)* (1/2)) - (1/2)) #formula for side length of ocatgon
radius = sqrt(pi)/pi
segmentHeight = radius - (sqrt((radius**2)-((chordLength/2)**2)))
sectorAngle = 2 * (acos((radius-segmentHeight)/radius))
arcLength = radians(radius * sectorAngle)
segmentArea = ((radius * arcLength) - (chordLength * (radius - segmentHeight)))/2
finalAnswer = segmentArea * -29388
print(f"{finalAnswer:.0f}")
