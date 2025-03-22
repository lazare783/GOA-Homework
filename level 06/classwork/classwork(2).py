x = int(input("enter number : "))
y = 0
for i in range(2,x):
     if x % i ==0 and y ==0:
          print("your number is not a prime")
          y +=1
if y == 0:
     print(" your number is a prime")