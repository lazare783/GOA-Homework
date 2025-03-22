x = input("enter word: ")
y =""
for i in x:
    if len(x) == 3:
        y=i+y
    else:
        print("you have to enter 3 numbers")
        x = input("enter word: ")
if y[0] == y[2]:
    print(True)
else:
    print(False)