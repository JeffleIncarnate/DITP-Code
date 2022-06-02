# inheratance Example

class Reptile:
    def __init__(self, length):
        self.length = length


class Snake(Reptile):
    def __init__(self, length):
        super().__init__(length)
        
    def info(self):
        return f"I am a snake. I am {self.length} meters long."

s1 = Snake(15)
print(s1.info())
