#while and for loops, no do while
#non-determinstic loop, use while, for loop, specific number of times.

#syntax
'''while condition:
    statement1
    statement2'''

i=1

while i <= 10:
    print(i)
    i += 1


num = int(input('\n Number to find factorial'))
fact = 1
num1 = num
while num > 0:
    fact = fact * num
    num -= 1

print(num1, ' factorial number is ', fact)







    





