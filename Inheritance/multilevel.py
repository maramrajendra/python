#Multi level inheritance

class Animal:

    def Food(self):
        print("Animal eats food to survive")

class Aquatic(Animal):
    def Habitat(self):
        print('Like to live in water')

class Shark(Aquatic):
    def Swim(self):
        print('Like to swim')

def main():
    shark = Shark()

    shark.Food()
    shark.Habitat()
    shark.Swim()

main()