class Alumno:

    tipo = "Alumno" # Atributo de clase

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre  # Atributos de objetos
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"{self.apellido}-{self.nombre}"
    
    def saludar(self):
        return f"Hola soy {self.nombre} y tengo {self.edad} años"


pepe = Alumno("jose", "perez", 25)
maria = Alumno("maria", "gomez", 33)

print(pepe.nombre, pepe.apellido, pepe.edad)
print(maria.nombre, maria.apellido, maria.edad)
print(pepe.saludar())
print(maria.saludar())

print(f"El tipo del objeto Pepe es {pepe.tipo}")
print(f"El tipo del objeto Maria es {maria.tipo}")


print(type(pepe))