#if cond, there won't be any start and end block, it is handled by indentation.


num = int(input('enter num:'))
if(num > 0):
    print('is positive number')

if(num > 0):
    print('in if block')
    print('is positive number')
else:
    print('in else block')
    print('not positive number')