import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Ejemplo Tkinter - 6 widgets")
    root.geometry("420x320")
    root.resizable(False, False)

    # Label
    label = ttk.Label(root, text="Ingrese su nombre:")
    label.grid(row=0, column=0, padx=12, pady=12, sticky="w")

    # Entry
    nombre_var = tk.StringVar()
    entry_nombre = ttk.Entry(root, textvariable=nombre_var, width=30)
    entry_nombre.grid(row=0, column=1, padx=12, pady=12, sticky="w")

    # Checkbutton
    suscribe_var = tk.BooleanVar(value=False)
    check_suscribe = ttk.Checkbutton(
        root,
        text="Suscribirme al boletín",
        variable=suscribe_var,
    )
    check_suscribe.grid(row=1, column=0, padx=12, pady=6, columnspan=2, sticky="w")

    # Radiobuttons
    opcion_var = tk.StringVar(value="opcion1")
    radio_frame = ttk.LabelFrame(root, text="Elige una opción")
    radio_frame.grid(row=2, column=0, padx=12, pady=6, columnspan=2, sticky="ew")

    rb1 = ttk.Radiobutton(radio_frame, text="Opción 1", variable=opcion_var, value="opcion1")
    rb2 = ttk.Radiobutton(radio_frame, text="Opción 2", variable=opcion_var, value="opcion2")
    rb1.grid(row=0, column=0, padx=10, pady=4, sticky="w")
    rb2.grid(row=0, column=1, padx=10, pady=4, sticky="w")

    # Listbox
    ttk.Label(root, text="Selecciona un color:").grid(row=3, column=0, padx=12, pady=6, sticky="w")
    list_colores = tk.Listbox(root, height=4, exportselection=False)
    colores = ["Rojo", "Verde", "Azul", "Amarillo"]
    for color in colores:
        list_colores.insert(tk.END, color)
    list_colores.grid(row=4, column=0, padx=12, pady=4, sticky="nsew")
    list_colores.selection_set(0)

    # Button
    resultado = tk.StringVar(value="Aquí aparecerá tu selección")

    def mostrar_resultado():
        nombre = nombre_var.get().strip() or "[no ingresado]"
        suscribe = "Sí" if suscribe_var.get() else "No"
        opcion = opcion_var.get()
        seleccionado = list_colores.curselection()
        color = colores[seleccionado[0]] if seleccionado else "[ninguno]"
        resultado.set(
            f"Nombre: {nombre}\nSuscrito: {suscribe}\nOpción: {opcion}\nColor: {color}"
        )

    boton = ttk.Button(root, text="Mostrar selección", command=mostrar_resultado)
    boton.grid(row=4, column=1, padx=12, pady=12, sticky="n")

    # Message / Label como salida
    output_label = ttk.Label(root, textvariable=resultado, justify="left", relief="sunken")
    output_label.grid(row=5, column=0, padx=12, pady=10, columnspan=2, sticky="ew")

    root.columnconfigure(1, weight=1)
    root.mainloop()


if __name__ == "__main__":
    main()
