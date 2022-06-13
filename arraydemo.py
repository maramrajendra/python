#Array Example
#import the module
import array

#creating an array, i is datatype integer

# numbers = array.array("i", [1,2,3,4,5])

# for i in range(0, 4):
#     print(numbers[i])
# print('printing ended')

# for i in range(0, len(numbers)):
#     print(numbers[i])
# print('printing ended')

# insert and append to add into array
# pop and remove to remove the element in the array

a = array.array("d", [1.1,1.2,1.3])

a.insert(1,3.1)

# inserted at the position 1

a.append(5.5)

# for i in range(0, len(a)):
#     print(a[i])
# print('printing ended')

#pop to remove the element from array
print(a.pop(1))

#remove the first position
a.remove(1.2)

for i in range(0, len(a)):
    print(a[i])
print('printing ended')



