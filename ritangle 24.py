def seq(u,v):
    if u < 0:
        return - u - v
    if u >= 0:
        return u - v
    
count1 = 1
count2 = 1
actualCount = 0
list1 = [1,1]
while actualCount != 50:
    temp = seq(count2, count1)
    count1 = count2
    count2 = temp
    list1.append(temp)
    actualCount += 1

count1 = -1
count2 = 1
actualCount = 0
list2 = [-1,1]
while actualCount != 50:
    temp = seq(count2, count1)
    count1 = count2
    count2 = temp
    list2.append(temp)
    actualCount += 1

count1 = 1
count2 = -1
actualCount = 0
list3 = [1,-1]
while actualCount != 50:
    temp = seq(count2, count1)
    count1 = count2
    count2 = temp
    list3.append(temp)
    actualCount += 1

count1 = -1
count2 = -1
actualCount = 0
list4 = [-1,-1]
while actualCount != 50:
    temp = seq(count2, count1)
    count1 = count2
    count2 = temp
    list4.append(temp)
    actualCount += 1

finalList = []
for i in range(50):
    if list1[0] == list1[i] and list2[0] == list2[i] and list3[0] == list3[i] and list4[0] == list4[i]:
        finalList.append(i+1)
print(finalList)