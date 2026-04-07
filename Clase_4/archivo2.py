with open("archivo.txt", "a") as f:
    f.write("Segundo ejemplo!\n")
    for i in range(1,11):
        f.write(f"Linea del segundo ejemplo {i} \n")

print("Fin de programa")        