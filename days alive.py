#Days alive calculator:
import datetime as dt
year = int(input("What year were you born in (e.g. 1988) "))
month = int(input("What month were you born in (e.g. 07 for July) "))
day = int(input("What day were you born on (e.g. 02 for the 2nd) "))
bday = dt.datetime(year, month, day)
today = dt.datetime.now()
diff = today - bday
if diff.days != 1:
    print(f"You have been alive for {diff.days} days.")
else:
    print(f"You have been alive for {diff.days} day.")
print(f"You have been alive for {diff.days * 24} hours.")
print(f"You have been alive for {diff.days * 24 * 60} minutes.")
print(f"You have been alive for {diff.days * 24 * 60 * 60} seconds.")

    
