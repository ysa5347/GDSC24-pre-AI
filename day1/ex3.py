from sys import exit

def is_numeric(value):
    return value.replace('.', '', 1).isdigit() if '.' in value else value.isdigit()

w = input("tipe width... : ")
if not is_numeric(w):
    print("Invalid input. The variables must be numbers.")
    exit()
w = float(w)

h = input("tipe height... : ")
if not is_numeric(h):    
    print("Invalid input. The variables must be numbers.")
    exit()
h = float(h)

print(f"the area of triangle is : {w*h/2}")