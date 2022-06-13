print("Start of the program")
try:
    a = int(input("Enter value for a = "))
    b = int(input("Enter value for b = "))

    result = a/b

    print("Result =", result)

    raise Exception("This is some new exception")

except ZeroDivisionError as e:
    print("Zero Division Error")
    print(e)
except ValueError as e:
    print("Value Error")
    print(e)
    print(type(e))
except Exception as e:
    print("Exception Caught")
    print(e)

finally:
    print("final block executed")

print("\n End of the program")