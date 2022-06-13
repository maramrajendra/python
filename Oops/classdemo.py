# A simple example of class and object in python

#creating a class

class Sample:
    x=10
    y=20
    __z=30

    #method in class, self is non static mehtod
    def myfunc(self):
        print("hello from the instance function")
    
    def Sum(self):
        print("Sum ", self.x+self.y)
    
    #static method
    @staticmethod
    def mynewfunc():
        print("Hell from a static function". __z)


def main():
    #creating object of class Sample
    s1 = Sample()

    #Accessing the member of the class
    print(s1.x, s1.y)

    s1.Sum()

main()


# __z variable is private and accessed through static methos