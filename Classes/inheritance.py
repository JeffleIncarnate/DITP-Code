# inheratance Example


class Reptile:
    def __init__(self, length):
        self.length = length


class Snake(Reptile):
    def __init__(self, length, weight):
        self.weight = weight


s1 = Snake()
