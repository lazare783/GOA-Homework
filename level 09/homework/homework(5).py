number = int(input("enter number: "))
def simple_multiplication(number) :
    if number%2==0:
        return number*8
    else:
        return number*9
print(simple_multiplication(number))