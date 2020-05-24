def mult():
    """This function multiplicities two integers"""
    a = int(input("Enter the value for 'a':"))
    b = int(input("Enter the value for 'b':"))
    return a * b


def show_result():
    """This function shows us a result of last multiplication"""
    return str("Result:") + str(mult())


print(show_result())
