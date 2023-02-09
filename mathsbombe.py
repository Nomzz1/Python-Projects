from random import sample
listOfNames = ["Aaron","Mohammed Yusuf","Tommaso","Vishni","Salma","Shamel","Azeem","Oliver","Taran","Ben","Alice","Sakshi"]
finalTeams = {}
for _ in range(3):
    team = sample(listOfNames,4)
    for i in team:
        listOfNames.remove(i)
    finalTeams.update({f"Team {_+1}":team})

for keys, values in finalTeams.items():
    print(f"{keys}: {values}")