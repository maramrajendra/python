#syntax wise fine but run time will get the error
# here python is handling runtime below error

# print("Start of the program")

# a = int(input("Enter value for a = "))
# b = int(input("Enter value for b = "))

# result = a/b

# print("Result =", result)

# print("\n End of the program")

# Syntax:

# try:
#      //statements
# except:
#     //message
# finally:
#     //statement - whatever code write it always executed whether error or not
#     //example - You can close the database connection

print("Start of the program")
try:
    a = int(input("Enter value for a = "))
    b = int(input("Enter value for b = "))

    result = a/b

    print("Result =", result)
except Exception as e:
    print("Something went wrong, please try again")
    print(e)
    print(type(e))
finally:
    print("final block executed")

print("\n End of the program")


