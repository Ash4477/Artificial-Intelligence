list1 = []
list2 = []

while (True):
    list1.append(int(input("Enter number for list 1: ")))
    if (input("Enter again? (y/n)") == 'n'):
        break

while (True):
    list2.append(int(input("Enter number for list 2: ")))
    if (input("Enter again? (y/n)") == 'n'):
        break

list3 = list1 + list2
list3.sort()

print("Smallest Value: ",list3[0],"\nLargest Value: ",list3[-1])