# main.py
import tkinter as tk
from tkinter import ttk, filedialog
from boleteo import iniciar_boleteo, cerrar_ventana, seleccionar_archivo_excel

if __name__ == "__main__":
    # Crear una tabla para pasar como argumento a la función
    tabla_inicial = tk.Tk()
    tabla_inicial.withdraw()
    seleccionar_archivo_excel(tabla_inicial)
