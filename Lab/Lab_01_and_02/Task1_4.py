marks = int(input("Enter your marks: "))

while (True):
    if (marks < 1) or (marks > 100):
        print("Invalid Score! :<")
        marks = int(input("Re-enter your marks: "))
    else:
        break

if (marks < 50):
    print("Grade: F")
elif (marks < 60):
    print("Grade: E")
elif (marks < 70):
    print("Grade: D")
elif (marks < 80):
    print("Grade: C")
elif (marks < 90):
    print("Grade: B")
else:
    print("Grade: A")
