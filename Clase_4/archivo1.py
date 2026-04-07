with open("archivo.txt", "w") as f:
    f.write("Hola Mundo!\n")
    for i in range(1,11):
        f.write(f"Linea {i} \n")

print("Fin de programa")        