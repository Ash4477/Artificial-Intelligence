birthdays = {
    "Oppenheimer" : "16th July",
    "Mehmood"  : "9th March",
    "Batman"  : "11th November",
    "Naruto"  :   "12th January"
}


print("Welcome to the birthday dictionary. We know the birthdays of: ")
for keys in birthdays.keys():
    print(keys)
bdayKey = input("Who's birthday do you want to look up? ")
print(bdayKey+"'s birthday is "+birthdays[bdayKey])