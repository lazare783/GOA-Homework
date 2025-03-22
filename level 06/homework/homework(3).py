print("password must have over 8 characters, one big letter and 1 number ")
password = input("enter password: ")
x=0
while len(password)<8 or "A" not in password:
    x+=1
    password = input("enter password: ")
    if x == 2:
         print("u get incorrect password 3 times")
         break
    if password == True:
        print("correct")