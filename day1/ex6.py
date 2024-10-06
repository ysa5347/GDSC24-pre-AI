ipt = input("tipe variables... : ").split(',')
if len(ipt) != 2:
    print("Invalid input. The count of variables must be 2.")
    exit()
a, b = ipt

print(f"the variables before swap are {a} and {b}.")
a, b = b, a
print(f"the variables after swap are {a} and {b}.")