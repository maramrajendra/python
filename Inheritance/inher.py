# Single Level
# Multi Level
# Multiple
# Hybrid
# Hierarchical

#single level

#Parent class
class Animal:

    def Habitat(self):
        print('Animal Habitat')


#child class, in brackets inheritance
class Dog(Animal):

    def Bark(self):
        print('Dog barking')

def main():
    d= Dog()

    d.Habitat()
    d.Bark()

main()