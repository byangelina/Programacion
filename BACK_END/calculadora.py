
#librerias
import tkinter as tk
from tkinter import messagebox

#ventana
ventana = tk.Tk()
ventana.title("================= Calculadora de Velocidad =================")
ventana.geometry("600x400")


#datos
tk.Label(ventana, text="Ingrese distancia (metros): ").pack()
distancia = tk.Entry(ventana)
distancia.pack()

tk.Label(ventana, text="Ingrese tiempo (segundos): ").pack()
tiempo = tk.Entry(ventana)
tiempo.pack()


#programa
def calcular():
    valor_distancia = distancia.get()
    valor_distancia = float(valor_distancia)
    valor_tiempo = tiempo.get()
    valor_tiempo = float(valor_tiempo)

    if valor_tiempo == 0:
        resultado.config(text="Error: el tiempo no puede ser cero")
    else:
        velocidad = valor_distancia / valor_tiempo
        resultado.config(text=f"La velocidad es: {velocidad} m/s")



boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()
    


















