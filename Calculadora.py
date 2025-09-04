import tkinter as tk
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("350x350")
etiqueta = tk.Label(ventana, text="Escribe los números:")
etiqueta.pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1 + num2}")
    except ValueError:
        resultado.config(text=f"Error: ingrese números válidos.")

def restar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1 - num2}")
    except ValueError:
        resultado.config(text=f"Error: ingrese números válidos.")

def multiplicar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1 * num2}")
    except ValueError:
        resultado.config(text=f"Error: ingrese números válidos.")

def dividir():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        if num2 != 0:
            resultado.config(text=f"Resultado: {num1 / num2}")
        else:
            resultado.config(text=f"Error: división por cero.")
    except ValueError:
        resultado.config(text=f"Error: ingrese números válidos.")

def limpiar():
        entrada1.delete(0, tk.END)
        entrada2.delete(0, tk.END)
        resultado.config(text="Resultado: ")

boton_sumar = tk.Button(ventana, text="+", command=sumar)
boton_sumar.pack(pady=5)
boton_restar = tk.Button(ventana, text="-", command=restar)
boton_restar.pack(pady=5)
boton_multiplicar = tk.Button(ventana, text="*", command=multiplicar)
boton_multiplicar.pack(pady=5)
boton_dividir = tk.Button(ventana, text="/", command=dividir)
boton_dividir.pack(pady=5)
boton_limpiar = tk.Button(ventana, text="AC", command=limpiar)
boton_limpiar.pack(pady=5)
boton_salir = tk.Button(ventana, text="Salir", command=exit)
boton_salir.pack(pady=5)

ventana.mainloop()