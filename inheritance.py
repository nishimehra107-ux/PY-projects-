class Animal:
    def __init__(self,name):
        self.name= name
        self.is_alive= True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is woofing")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")

dog=Dog("buddy")
cat=Cat("cosmo")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.bark()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.meow()