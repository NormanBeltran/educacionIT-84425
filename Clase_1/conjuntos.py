"""
Conjuntos: { elem1, elem2 ... elemN  }

1. Orden NO (no trabajamos con indices numericos)
2. Mutabilidad SI (parcialmente solo eliminar/agregar) 
3. Repetición de elementos NO

"""

c1 = {1,2,3,4,5}
c2 = {4,5,6,7,8}

# Union
print(c1.union(c2)) # c1 | c2 

# Interseccion

print(c1.intersection(c2)) # c1 & c2

# Diferencia
print(c1.difference(c2)) # c1 - c2

# Diferencia simétrica
print(c1.symmetric_difference(c2)) # c1 | c2 - (c1 & c2)