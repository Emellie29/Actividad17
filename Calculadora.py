import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x300")
etiqueta1 = tk.Label(ventana, text="Escribe el primer número:")
etiqueta1.pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)
etiqueta2 = tk.Label(ventana, text="Escribe el segundo número:")
etiqueta2.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)
num1 = 0
num2 = 0
def sumar(num1, num2):
    resultado = num1 + num2
    return resultado
def restar(a,b):
    numero = entrada1.get()+entrada2.get()
boton_sumar = tk.Button(ventana, text="+", command=sumar)
boton_sumar.pack(pady=5)

ventana.mainloop()