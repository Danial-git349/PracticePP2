#Example1
class Flyer:
    def fly(self):
        print("I can fly!")

class Swimmer:
    def swim(self):
        print("I can swim!")

class Duck(Flyer, Swimmer):
    pass

donald = Duck()
donald.fly()
donald.swim()
#Example2
class Flyer:
    def move(self):
        print("I fly in the sky")

class Swimmer:
    def move(self):
        print("I swim in the water")

class Duck(Flyer, Swimmer):
    pass

donald = Duck()
donald.move()

#Example3
class Flyer:
    def move(self):
        print("I fly in the sky")

class Swimmer:
    def move(self):
        print("I swim in the water")

class Duck(Flyer, Swimmer):
    def move(self):
        print("I can both fly and swim")

donald = Duck()
donald.move()


