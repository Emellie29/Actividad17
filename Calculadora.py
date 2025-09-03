import tkinter as tk
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")
etiqueta1 = tk.Label(ventana, text="Escribe el primer número:")
etiqueta1.pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)
etiqueta2 = tk.Label(ventana, text="Escribe el segundo número:")
etiqueta2.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)
etiqueta3 = tk.Label(ventana, text="Mostrar Resultado:")
etiqueta3.pack(pady=5)
entrada3 = tk.Entry(ventana)
entrada3.pack(pady=5)
def sumar():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    result = a + b
    etiqueta3.config(text=f"El resultado es: {result}")
def restar(a,b):
    numero = entrada1.get()+entrada2.get()
boton_sumar = tk.Button(ventana, text="+", command=sumar)
boton_sumar.pack(pady=5)

ventana.mainloop()