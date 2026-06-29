class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("{} says  Woof Woof!".format(self.name))

Puppy = Dog("Buddy", "Golden Retriever")

Puppy.bark()

class phone:
    def __init__(self, battery):
        self.battery = battery

    def use_phone(self):
        self.battery -= 5
        print("battery is now {}%".format(self.battery))

Samsung = phone(100)

for i in range(3):
    Samsung.use_phone()

# KEY POINTS

#Encapsulation: Classes encapsulate their attributes by using self.

#Inheritance: Classes can inherit from other classes,
#allowing for code reuse and the creation of subclasses.

#Polymorphism: Classes can have methods with the same name but different implementations,
#allowing for more options in how objects are used.