class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("Dhruv", 15)
print(p1.__sizeof__())

for i in p1.__dict__.keys():
    print(i)