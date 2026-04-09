# Herencia

class ClaseA:
    def __init__(self):
        self.a = 1


class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()
        self.b = 2

obj = ClaseB()

print(obj.a, obj.b)