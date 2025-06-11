# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is currently eating.")

    def sleep(self):
        print(f"{self.name} is currently sleeping.")

class Dog(Animal):
    def speak(self):
        print("WOOF WOOF WOOF WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW MEOW MEOW MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK SQUEEK SQUEEK SQUEEK")

dog = Dog("Scooby-Doo")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(f"It is {dog.is_alive} that {dog.name}is alive and full of energy.")
print(f"It is {cat.is_alive} that {cat.name}is alive and full of energy.")
print(f"It is {mouse.is_alive} that {mouse.name}is alive and full of energy.")

dog.speak()
cat.speak()
mouse.speak()


