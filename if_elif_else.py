def func_if_else(x, y, z):
    """This function makes the comparisons of integers"""
    if x > y:
        print("Свершилось!")
    elif y > x:
        print("Да ну!")
    else:
        print("А если так?")
        func_if_else(x + z, y - z, z)


a = int(input("Введите значение А: "))
b = int(input("Введите значение Б: "))
c = int(input("Введите значение В: "))
func_if_else(a, b, c)





