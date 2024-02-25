n = int(input("Enter number of terms: "))
num1 = 0
num2 = 1
print(num1,num2,end=" ")
counter = 0
while (counter < n):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3, end=" ")
    counter += 1