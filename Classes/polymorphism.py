"""
Polymorphism is a very important concept in programming. 
It refers to the use of a single type entity 
    (method, operator or object) to represent different types in different scenarios
"""

# Polymorphism for adding nums 
num1 = 1
num2 = 3
print(num1 + num2)

# Polymorphism with string literals
str1 = "Python"
str2 = "Programming"
print(str1 + " " + str2)

# Polymorphism with Classes

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()