import tkinter as tk
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("250x250")
etiqueta = tk.Label(ventana, text="Escribe los números:", font=("Helvetica", 12, "bold"), fg="sky blue")
etiqueta.pack(pady=5)
entrada1 = tk.Entry(ventana, font=("Calibri", 12))
entrada1.pack(pady=5)
entrada2 = tk.Entry(ventana, font=("Calibri", 12))
entrada2.pack(pady=5)
resultado = tk.Label(ventana, text="Resultado:", font=("Helvetica", 12, "bold"), fg="violet")
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
#mantener los botos agrupados sin alterar la funcion principal
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)
#.grid() posiciona los botones en filas y columnas para mejor control
# #width,padx,pady aseguran que los botones se vean bien alineados
boton_sumar = tk.Button(frame_botones, text="+", command=sumar, width=8, font=("Courier", 8, "bold"), bg="pink")
boton_sumar.grid(row=0, column=0, padx=5, pady=5)
boton_restar = tk.Button(frame_botones, text="-", command=restar, width=8, font=("Courier", 8, "bold"), bg="pink")
boton_restar.grid(row=0, column=1, padx=5, pady=5)
boton_multiplicar = tk.Button(frame_botones, text="*", command=multiplicar, width=8, font=("Courier", 8, "bold"), bg="pink")
boton_multiplicar.grid(row=0, column=2, padx=5, pady=5)
boton_dividir = tk.Button(frame_botones, text="/", command=dividir, width=8, font=("Courier", 8, "bold"), bg="pink")
boton_dividir.grid(row=1, column=0, padx=5, pady=5)
boton_limpiar = tk.Button(frame_botones, text="AC", command=limpiar, width=8, font=("Courier", 8, "bold"), bg="pink")
boton_limpiar.grid(row=1, column=1, padx=5, pady=5)
boton_salir = tk.Button(frame_botones, text="Salir", command=exit, width=8, font=("Courier", 8, "bold"), bg="pink")
boton_salir.grid(row=1, column=2, padx=5, pady=5)

ventana.mainloop()