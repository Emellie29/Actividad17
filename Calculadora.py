import tkinter as tk
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")
etiqueta = tk.Label(ventana, text="Escribe el primer número:")
etiqueta.pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

ventana.mainloop()