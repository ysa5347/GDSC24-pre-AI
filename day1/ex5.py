from sys import exit

def is_numeric(value):
    return value.replace('.', '', 1).isdigit() if '.' in value else value.isdigit()

contents = input("tipe coefficients... : ").split(',')
if len(contents) != 3:
    print("Invalid input. The coefficients must be 3 numbers.")
    exit()
for content in contents:
    try:
        float(content)
    except:
        print(f"Invalid input. The coefficients must be numbers. {content}")
        exit()

a, b, c = contents 

if a == '0':
    print("The coefficient of x^2 must not be 0.")
    exit()
a, b, c = float(a), float(b), float(c)

D = b**2 - 4*a*c
if D < 0:
    print("There is no real root.")
elif D == 0:
    x = -b / (2*a)
    print(f"The root is {x}.")
else:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print(f"The roots are {x1} and {x2}.")