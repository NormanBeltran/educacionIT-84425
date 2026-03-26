amigos = ["juan", "ana", "maria", "pedro"]
edades = [20, 30, 40, 50]
dnis = [123, 456, 789, 987]

for a, e, d in zip(amigos, edades, dnis):   
    print(f"{a} {e} {d}")
