from tkinter import *

#import tkinter as tk

def btn_presionado():
    try:
        n1 = int(text.get())
        n2 = int(text1.get())
        print(f"Valores {n1} y {n2}")
        resultado.config(text=str(n1+n2))

    except Exception as e:
        print("Alguno de los valores NO es numerico")

    

window = Tk()
window.title("Bienvenidos Tkinter")
window.config(width=400, height=200)

lbl = Label(window, text="Ingresa número (1):")
lbl.place(x=50, y=10)

text = Entry(window)
text.place(x=200, y=10)

lbl1 = Label(window, text="Ingresa número (2):")
lbl1.place(x=50, y=40)


text1 = Entry(window)
text1.place(x=200, y=40)

resultado = Label(window, text="", font=("Arial Bold", 50))
resultado.place(x=200, y=80)

boton = Button(window, text="Sumar", command=btn_presionado)
boton.place(x=100, y=80)

window.mainloop()