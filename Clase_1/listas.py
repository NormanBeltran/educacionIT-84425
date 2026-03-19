"""
Listas:

1. Orden SI
2. Mutabilidad SI
3. Repetición de elementos SI

"""

amigos = [ "Juan", "Ana", "Pedro", "Maria", "Juan" ]

# Orden

print(amigos[2])

# Mutabilidad

amigos.append("Juana")  # Agregar un elemento al final
amigos.insert(1, "Pablo") # Insertar un elemento desde una posición

del amigos[0] # Eliminar un elemento desde su posición
amigos.pop(3) # Eliminar un elemento desde su posición

amigos[0] = "Juan Pablo"


print(amigos)