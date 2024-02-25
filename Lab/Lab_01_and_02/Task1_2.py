sumEven = 0
sumOdd = 0
inputCheck = False

while (True):
    inp = int(input("Enter Integer: "))
    if (int(inp)%2 == 0):
        sumEven += inp
    else:
        sumOdd += inp
    checker = input("Enter again? (y/n) ")
    if (checker == 'n'):
        break

print("\nSum Of Even Integers: ", sumEven,
      "\nSum Of Odd Integers: ", sumOdd)