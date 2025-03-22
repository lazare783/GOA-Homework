print("password must have over 8 characters, one big letter and 1 number ")
password = input("enter password")
while len(password)<8 or "A" not in password:
    password = input("enter password: ")
print("correct")