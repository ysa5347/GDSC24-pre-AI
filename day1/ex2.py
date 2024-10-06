from sys import exit

def is_numeric(value):
    return value.replace('.', '', 1).isdigit() if '.' in value else value.isdigit()

a = input("tipe first variable... : ")
if not is_numeric(a):
    print("Invalid input. The variables must be numbers.")
    exit()
a = float(a)

b = input("tipe second variable... : ")
if not is_numeric(b):    
    print("Invalid input. The variables must be numbers.")
    exit()
b = float(b)

op = input("tipe operator...(+/*) : ")

if op != '+' and op != '*' :
    print("Invalid operator")
elif op == '+':
    print(a+b)
    exit()
else:
    print(a*b)
    exit()