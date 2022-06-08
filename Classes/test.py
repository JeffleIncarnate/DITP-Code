class Person:
    def __init__(self, height, age, name, job):
        self.height = height
        self.age = age
        self.name = name
        self.job = job


class Teacher(Person):
    def __init__(self, height, age, name, job):
        super().__init__(height, age, name, job)


class Student(Person):
    def __init__(self, height, age, name, job):
        super().__init__(height, age, name, job)


t1 = Teacher(180, 30, "Mr. Bang", "Teacher")

MrBang__Dictionary = t1.__dict__

print("Teacher: ")
for key, value in MrBang__Dictionary.items():
    print("{}: {}".format(key, value))
print("")

s1 = Student(172, 15, "Sonny", "Student")

Sonny__Dictionary = s1.__dict__

print("Student: ")
for key, value in Sonny__Dictionary.items():
    print("{}: {}".format(key, value))
print("")
