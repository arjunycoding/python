from datetime import date

birthyear = input('what year were you born? ')
todays_year = date.today().year
age = todays_year - int(birthyear)
print(f"You are {age} years old")