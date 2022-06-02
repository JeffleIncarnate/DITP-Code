# OOP with classes
class Music:
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration

    def return_data(self):
        return f"{self.artist} - {self.title} - {self.duration}"

m1 = Music("Will wood", "2econd 2ight 2eer", "100")

for item in m1.__dict__:
    print("{}: {}".format(item, m1.__dict__[item]))

# OOP with variables
num1 = 10.10

floored = num1.__floor__()
print(floored)