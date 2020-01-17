class Dog:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = int(age)
    
    def woof(self):
        print("{} Woofs!".format(self.name))
    
    def birthday(self):
        self.age = self.age + 1
        print("{} just turned {} years old!".format(self.name, str(self.age)))

Dogs = []
for i in range(2):
    name = input("Name: ")
    age = input("Age: ")
    Dogs.append(Dog(name, age))


print("{} is a dog that is {} years old!".format(Dogs[0].name, Dogs[0].age))
Dogs[0].woof()
Dogs[1].birthday()
