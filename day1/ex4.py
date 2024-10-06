from sys import exit

def is_integer(value):
    try:
        int(value)
        return True
    except:
        return False

a = input("tipe variable... : ")
if not is_integer(a):
    print("Invalid input. The variables must be integer.")
    exit()
a = int(a)

if a % 2 == 0:
    print(f"{a} is an even number.")
else:
    print(f"{a} is an odd number.") 