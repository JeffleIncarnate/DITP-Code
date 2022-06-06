# Constructor Example
class Person:
    def __init__(self, age, height, name):
        self.name = name
        self.age = age
        self.height = height

    # Constructor Example
    def pritn_name_age(self):
        print(
            "My name is {}, i am {} years old, I am {}cm tall".format(
                self.name, self.age, self.height
            )
        )


dhruv = Person(15, 169, "Dhruv")
dhruv.pritn_name_age()
