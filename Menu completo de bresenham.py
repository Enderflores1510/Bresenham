import tkinter as tk
from tkinter import messagebox

def option1():
    messagebox.showinfo("linea de Bresenham", "Has seleccionado la opción linea de bresenham")
        
    def dibujar_bresenham():
        try:
            x0 = int(entry_x0.get())
            y0 = int(entry_y0.get())
            x1 = int(entry_x1.get())
            y1 = int(entry_y1.get())

            # Limpiar el canvas antes de dibujar una nueva línea
            canvas.delete("linea")

            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            sx = 1 if x0 < x1 else -1
            sy = 1 if y0 < y1 else -1
            err = dx - dy

            while True:
                canvas.create_rectangle(x0, y0, x0 + 1, y0 + 1, fill="black", tags="linea")

                if x0 == x1 and y0 == y1:
                    break

                e2 = 2 * err
                if e2 > -dy:
                    err -= dy
                    x0 += sx
                if e2 < dx:
                    err += dx
                    y0 += sy

        except ValueError:
            messagebox.showerror("Error", "Ingrese coordenadas válidas (números enteros).")

# Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Algoritmo de Bresenham")

# Etiquetas y entradas para las coordenadas
    tk.Label(ventana, text="Punto inicial (x, y):").grid(row=0, column=0, columnspan=2)
    tk.Label(ventana, text="x:").grid(row=1, column=0)
    entry_x0 = tk.Entry(ventana)
    entry_x0.grid(row=1, column=1)
    tk.Label(ventana, text="y:").grid(row=2, column=0)
    entry_y0 = tk.Entry(ventana)
    entry_y0.grid(row=2, column=1)

    tk.Label(ventana, text="Punto final (x, y):").grid(row=3, column=0, columnspan=2)
    tk.Label(ventana, text="x:").grid(row=4, column=0)
    entry_x1 = tk.Entry(ventana)
    entry_x1.grid(row=4, column=1)
    tk.Label(ventana, text="y:").grid(row=5, column=0)
    entry_y1 = tk.Entry(ventana)
    entry_y1.grid(row=5, column=1)

# Botón para dibujar la línea
    boton_dibujar = tk.Button(ventana, text="Dibujar línea", command=dibujar_bresenham)
    boton_dibujar.grid(row=6, column=0, columnspan=2)

# Canvas para dibujar la línea
    canvas = tk.Canvas(ventana, width=1920, height=625, bg="white")
    canvas.grid(row=7, column=0, columnspan=2)

# Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()

def option2():
    messagebox.showinfo("punto medio", "Has seleccionado la opción de unto medio")
    def algoritmo_punto_medio():
        """
        Función para dibujar una línea utilizando el algoritmo de punto medio.
        """
        try:
            x0 = int(entry_x0.get())
            y0 = int(entry_y0.get())
            x1 = int(entry_x1.get())
            y1 = int(entry_y1.get())

            # Limpiar el canvas
            canvas.delete("linea")

            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            sx = 1 if x0 < x1 else -1
            sy = 1 if y0 < y1 else -1

            if dy <= dx:  # Pendiente <= 1
                d = 2 * dy - dx
                incrE = 2 * dy
                incrNE = 2 * (dy - dx)

                x = x0
                y = y0

                while x != x1:
                    canvas.create_rectangle(x, y, x + 1, y + 1, fill="black", tags="linea")
                    if d < 0:
                        d += incrE
                        x += sx
                    else:
                        d += incrNE
                        x += sx
                        y += sy
                canvas.create_rectangle(x, y, x + 1, y + 1, fill="black", tags="linea")  # Dibuja el punto final

            else:  # Pendiente > 1
                d = 2 * dx - dy
                incrE = 2 * dx
                incrNE = 2 * (dx - dy)

                x = x0
                y = y0

                while y != y1:
                    canvas.create_rectangle(x, y, x + 1, y + 1, fill="black", tags="linea")
                    if d < 0:
                        d += incrE
                        y += sy
                    else:
                        d += incrNE
                        x += sx
                        y += sy
                canvas.create_rectangle(x, y, x + 1, y + 1, fill="black", tags="linea")  # Dibuja el punto final

        except ValueError:
            messagebox.showerror("Error", "Ingrese coordenadas válidas (números enteros).")

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Algoritmo de Punto Medio")

    # Etiquetas y entradas para las coordenadas
    tk.Label(ventana, text="Punto inicial (x, y):").grid(row=0, column=0, columnspan=2)
    tk.Label(ventana, text="x:").grid(row=1, column=0)
    entry_x0 = tk.Entry(ventana)
    entry_x0.grid(row=1, column=1)
    tk.Label(ventana, text="y:").grid(row=2, column=0)
    entry_y0 = tk.Entry(ventana)
    entry_y0.grid(row=2, column=1)

    tk.Label(ventana, text="Punto final (x, y):").grid(row=3, column=0, columnspan=2)
    tk.Label(ventana, text="x:").grid(row=4, column=0)
    entry_x1 = tk.Entry(ventana)
    entry_x1.grid(row=4, column=1)
    tk.Label(ventana, text="y:").grid(row=5, column=0)
    entry_y1 = tk.Entry(ventana)
    entry_y1.grid(row=5, column=1)

    # Botón para dibujar la línea
    boton_dibujar = tk.Button(ventana, text="Dibujar línea", command=algoritmo_punto_medio)
    boton_dibujar.grid(row=6, column=0, columnspan=2)

    # Canvas para dibujar la línea
    canvas = tk.Canvas(ventana, width=1920, height=625, bg="white")
    canvas.grid(row=7, column=0, columnspan=2)

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()    
        
def option3():
    messagebox.showinfo("Circunferencia", "Has seleccionado la opción de Circunferencia")
    def algoritmo_punto_medio_circunferencia():
        """
        Función para dibujar una circunferencia. 
        """
        try:
            centro_x = int(entry_centro_x.get())
            centro_y = int(entry_centro_y.get())
            radio = int(entry_radio.get())

            # Limpiar el canvas
            canvas.delete("circunferencia")

            x = 0
            y = radio
            d = 1 - radio

            while x <= y:
                dibujar_octante(centro_x, centro_y, x, y)
                if d < 0:
                    d += 2 * x + 3
                else:
                    d += 2 * (x - y) + 5
                    y -= 1
                x += 1

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos (números enteros).")

    def dibujar_octante(centro_x, centro_y, x, y):
        """
        Función auxiliar para dibujar los ocho octantes de la circunferencia.
        """
        canvas.create_rectangle(centro_x + x, centro_y + y, centro_x + x + 1, centro_y + y + 1, fill="black", tags="circunferencia")
        canvas.create_rectangle(centro_x - x, centro_y + y, centro_x - x + 1, centro_y + y + 1, fill="black", tags="circunferencia")
        canvas.create_rectangle(centro_x + x, centro_y - y, centro_x + x + 1, centro_y - y + 1, fill="black", tags="circunferencia")
        canvas.create_rectangle(centro_x - x, centro_y - y, centro_x - x + 1, centro_y - y - 1, fill="black", tags="circunferencia")
        canvas.create_rectangle(centro_x + y, centro_y + x, centro_x + y + 1, centro_y + x + 1, fill="black", tags="circunferencia")
        canvas.create_rectangle(centro_x - y, centro_y + x, centro_x - y + 1, centro_y + x + 1, fill="black", tags="circunferencia")
        canvas.create_rectangle(centro_x + y, centro_y - x, centro_x + y + 1, centro_y - x + 1, fill="black", tags="circunferencia")
        canvas.create_rectangle(centro_x - y, centro_y - x, centro_x - y + 1, centro_y - x + 1, fill="black", tags="circunferencia")

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Circunferencia")

    # Etiquetas y entradas para las coordenadas
    tk.Label(ventana, text="Centro (x, y):").grid(row=0, column=0, columnspan=2)
    tk.Label(ventana, text="x:").grid(row=1, column=0)
    entry_centro_x = tk.Entry(ventana)
    entry_centro_x.grid(row=1, column=1)
    tk.Label(ventana, text="y:").grid(row=2, column=0)
    entry_centro_y = tk.Entry(ventana)
    entry_centro_y.grid(row=2, column=1)

    tk.Label(ventana, text="Radio:").grid(row=2, column=0, columnspan=2)
    entry_radio = tk.Entry(ventana)
    entry_radio.grid(row=4, column=0, columnspan=2)

    # Botón para dibujar la circunferencia
    boton_dibujar = tk.Button(ventana, text="Dibujar circunferencia", command=algoritmo_punto_medio_circunferencia)
    boton_dibujar.grid(row=5, column=0, columnspan=2)

    # Canvas para dibujar la circunferencia
    canvas = tk.Canvas(ventana, width=1920, height=620, bg="white")
    canvas.grid(row=6, column=0, columnspan=2)

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()
root = tk.Tk()
root.title("Menú de Opciones")

menu = tk.Menu(root)
root.config(menu=menu)

options_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Opciones", menu=options_menu)
options_menu.add_command(label="Linea de bresenham", command=option1)
options_menu.add_command(label="punto medio", command=option2)
options_menu.add_command(label="Circunferencia", command=option3)

root.mainloop()