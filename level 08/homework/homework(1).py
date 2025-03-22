x = int(input("enter number: "))
for i in range(1,x+1):
    
    if x*i > 100:
        break
    elif x > 50:
        print("you have to enter number less than 50")
        break
    else:
        print(x*i)