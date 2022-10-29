weather = [["Jan",6,3],["Feb",7,3],["Mar",10,4],["Apr",13,6],["May",17,9],["Jun",20,12],["Jul",22,14],["Aug",21,14],["Sep",19,12],["Oct",14,9],["Nov",10,6],["Dec",7,3]]
print(sorted(weather, key = lambda item : item[1])[:6])
print([i for i in weather if i[2] < 9])
print([i for i in weather if i[1] >= 20])
