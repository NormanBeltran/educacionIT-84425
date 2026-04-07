nombre = "Jose"
edad = 25

mensaje = "Bienvenido {} a la clase, sabemos que tu edad es {}"
print(mensaje.format(nombre, edad))

mensaje1 = "Tu edad es {1} y tu nombre es {0}"
print(mensaje.format(nombre, edad))

print(f"Tu nombre es {nombre} y edad {edad} ")

saldo = 12345.98765

print(f"El saldo es: {saldo:>12.2f}")
print(f"El saldo es: {saldo:>10.2f}")
print(f"El saldo es: {saldo:<12.2f}")