def func_if_else(x, y, z,):
    if x > y:
        print("Done!")
    elif y > x:
        print("Really?!")
    else:
        print("How about this?")
        func_if_else(x + z, y - z, z)


a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))
func_if_else(a, b, c)

