# for loop with range

for i in range(10):
    print(i)

 #starts from 0 and < 10.

n = int(input('Input the number'))
for i in range(1,11):
    result = n * i
    print(result)

 #range(start, stop, increment)
 # stop will be less than stop value

n = int(input('Input the number'))
for i in range(1,11, 2):
    result = n * i
    print(result)

#even number multiples
print('increment by 2')
for i in range(2,11,2):
    print( n * i)