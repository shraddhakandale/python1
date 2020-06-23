a = 15
b = 3

try:
    print("resource open")
    print(a/b)
    x = int(input("enter a number"))
    print(x)
except ZeroDivisionError as e:
    print("cannot divide by zero" ,e)
except ValueError as e:
    print("invalid input",e)

finally:
    print("resource close")