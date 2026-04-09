class Empleado:

    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    # getters y setters

    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario

    def __str__(self):
        return f"{self.__nombre} - {self.__salario}"

ana = Empleado("Ana Perez", 3000)
print(ana)
print(ana.getSalario()) 

ana.setSalario(4500)
print(ana.getSalario()) 
