amigos = {"juan":28, "ana":45, "pedro":50, "maria": 34}

if "juan" in amigos:
    print("Juan es un amigo")

# No funciona de esta manera para los valores
if 28 in amigos:
    print("28 es un amigo")    
else:
    print("28 NO es un amigo")    

# Como consultar si un valor existe dentro de un diccionario
# 

if 28 in amigos.values():
    print("El valor 28 se encuentra en el Diccionario de amigos")    