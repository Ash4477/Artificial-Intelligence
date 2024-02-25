fact = int(input("Enter a number: "))
result = 1
counter = 1
while counter < fact:
    result *=  counter+1
    counter += 1

print (result)