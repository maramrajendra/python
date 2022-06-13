#python property example

class Person:
    def __init__(self, name):
        self.name=name

# getter
    @property
    def name(self):
        print("Returnin a valud")
        return self.__name

#setter
    @name.setter
    def name(self, value):
        print('setting the value')
        self.__name = value
    
person = Person('Raj')
print(person.name)

person.name = 'Rajendra'
print(person.name)