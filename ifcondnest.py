#comparing 3 numbers with nested if

num1 = int(input('Enter number1:'))
num2 = int(input('Enter number2:'))
num3 = int(input('Enter number3:'))


if(num1 > num2 and num1 > num3):
    print('num1 is greater:', num1)
elif(num2 > num3):
    print("num2 is greater:", num2)
else:
    print("num3 is greater:", num3)


