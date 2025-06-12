# multiple inheritance = inherit from more than one parent class
#                        C(A,B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                         C(B) <- B(A) <- A



# multiple inheritance

class Prey:# Parent
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} is running")

class Predator: # Parent
    def __init__(self, name):
        self.name = name

    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.run()
hawk.hunt()
fish.run()
fish.hunt()

# multilevel inheritance

class Animal: # Grandparent
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is eating")

class Prey(Animal): # Parent
    def run(self):
        print(f"{self.name} is running")

class Predator(Animal): # Parent
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
hawk.sleep()
