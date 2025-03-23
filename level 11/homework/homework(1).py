x = int(input('enter first number: '))
op = input('enter sign:')
y = int(input('enter second number:'))

def calculator(x, y, op):
    if type(x)!=int or type(y)!=int:
        return 'unknown value'
    elif op == "+":
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