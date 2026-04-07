with open("archivo.txt", "r") as f:
    f.seek(100)
    linea = f.readline()

    while linea:
        print(linea, end="")
        linea = f.readline()

print("Fin de programa")     