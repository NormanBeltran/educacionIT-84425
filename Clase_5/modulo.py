class ClaseA:
    def __init__(self):
        self.a = 1


class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()
        self.b = 2

def f(x,y):
    return x**2+y**2

paises = ["ARG", "URU", "BRA", "PER"]
