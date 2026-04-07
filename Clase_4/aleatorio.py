import random 


poblacion = ["ana", "juan", "pedro", "jose", "maria", "veronica"]

for i in range(5):
    print(random.sample(poblacion, k=3))