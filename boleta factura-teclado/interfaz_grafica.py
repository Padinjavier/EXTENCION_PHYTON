# interfaz_grafica.py
import tkinter as tk
from tkinter import ttk, filedialog
from boleteo import leer_excel, actualizar_tabla, ejecutar_codigo, cerrar_ventana, iniciar_boleteo

def seleccionar_archivo_excel(tabla):
    def seleccionar_archivo():
        # Abre el cuadro de diálogo para seleccionar el archivo
        archivo_excel = filedialog.askopenfilename(
            title="Seleccionar Archivo Excel",
            filetypes=[("Archivos Excel", "*.xlsx;*.xls")]
        )
        entry_archivo.delete(0, tk.END)
        entry_archivo.insert(0, archivo_excel)

        # Lee los datos del archivo Excel
        datos = leer_excel(archivo_excel)

        # Si se pudieron leer los datos, actualiza la tabla
        if datos is not None:
            actualizar_tabla(tabla, datos)

    def crear_ventana_resultado():
        # Crea una nueva ventana para mostrar el resultado
        ventana_resultado = tk.Toplevel(ventana_seleccion)
        ventana_resultado.title("Resultado")

        # Etiqueta y botón de "Listo"
        label_listo = tk.Label(ventana_resultado, text="Listo")
        label_listo.pack(pady=10)

        boton_cerrar = tk.Button(ventana_resultado, text="Cerrar", command=lambda: cerrar_ventana(ventana_resultado))
        boton_cerrar.pack(pady=10)

        # Oculta la ventana principal durante la ejecución
        ventana_seleccion.withdraw()

        # Inicia el boleteo con la nueva ventana de resultado
        iniciar_boleteo(tabla, ventana_resultado)

    # Crea una ventana tkinter para la selección de archivo
    ventana_seleccion = tk.Tk()
    ventana_seleccion.title("Selección de Archivo Excel")



    # Etiqueta y entrada para mostrar el nombre del archivo
    label_archivo = tk.Label(ventana_seleccion, text="Archivo Excel:")
    label_archivo.grid(row=0, column=0, padx=10, pady=10)

    entry_archivo = tk.Entry(ventana_seleccion, width=50)
    entry_archivo.grid(row=0, column=1, padx=10, pady=10)

    # Botón para seleccionar archivo
    boton_seleccionar = tk.Button(ventana_seleccion, text="Seleccionar Archivo", command=seleccionar_archivo)
    boton_seleccionar.grid(row=0, column=2, padx=10, pady=10)

    # Crear una tabla para mostrar los datos
    tabla = ttk.Treeview(ventana_seleccion)
    tabla["columns"] = ("Unidades", "Nombres", "Precios", "IGV" ,"PRE IGV", "aaa")
    tabla["show"] = "headings"

    # Configurar las columnas
    for columna in tabla["columns"]:
        tabla.heading(columna, text=columna)
        tabla.column(columna, anchor="center")

    # Mostrar la tabla
    tabla.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Botón para iniciar el boleteo
    boton_iniciar_boleteo = tk.Button(ventana_seleccion, text="Iniciar Boleteo", command=crear_ventana_resultado)
    boton_iniciar_boleteo.grid(row=2, column=1, pady=10)


    # Ejecuta el bucle de la interfaz gráfica
    ventana_seleccion.mainloop()
