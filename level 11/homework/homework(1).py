x = int(input('enter first number: '))
op = input('enter sign:')
y = int(input('enter second number:'))

def calculator(x, y, op):
    if op == "+":
        return x+y
    elif op == "-":
        return x-y
    elif op == "*":
        return x*y
    elif op == "/":
        return x/y
    else:
        return "unknown value"
    
print(calculator(x,y,op))