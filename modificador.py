import pandas as pd
from tkinter import Tk, filedialog, Button, Label
from fuzzywuzzy import process

def obtener_mejor_coincidencia(nombre_producto, productos_excel):
    # Encuentra la mejor coincidencia en la lista de productos_excel
    mejor_coincidencia, _ = process.extractOne(nombre_producto, productos_excel)
    return mejor_coincidencia

def procesar_excel():
    # Abrir el cuadro de diálogo para seleccionar el archivo Excel
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Excel files", "*.xlsx;*.xls")])

    # Verificar si se seleccionó un archivo
    if not file_path:
        return

    # Leer el archivo Excel
    df = pd.read_excel(file_path)

    # Leer la hoja "PRODUCTOS" del archivo "DATOS" en la misma carpeta
    productos_excel = pd.read_excel('DATOS.xlsx', sheet_name='PRODUCTOS')['PRODUCTO'].tolist()

    # Eliminar filas innecesarias (filas con valores nulos)
    df = df.dropna(subset=['NOTA PEDIDO', 'NOMBRE DEL CLIENTE', 'CANT', 'PRODUCTOS'], how='all')

    # Crear un nuevo DataFrame con las columnas requeridas
    new_df = df[['NOTA PEDIDO', 'NOMBRE DEL CLIENTE', 'CANT', 'PRODUCTOS']]

    # Sumar las dos columnas de precio unitario y colocar el resultado en una nueva columna
    new_df['PRECIO UNIT'] = df['PRECIO UNIT 1'].fillna(0) + df['PRECIO UNIT 2'].fillna(0)

    # Añadir la columna de Total
    new_df['TOTAL'] = new_df['CANT'] * new_df['PRECIO UNIT']

    # Añadir la columna de Producto Completo
    new_df['PRODUCTO COMPLETO'] = df['PRODUCTOS'].apply(lambda x: obtener_mejor_coincidencia(str(x), productos_excel))

    print("Resultados:")
    print(new_df[['NOTA PEDIDO', 'NOMBRE DEL CLIENTE', 'CANT', 'PRODUCTOS', 'PRODUCTO COMPLETO', 'PRECIO UNIT', 'TOTAL']])

    # Guardar el nuevo DataFrame en un nuevo archivo Excel
    new_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if new_file_path:
        new_df.to_excel(new_file_path, index=False)
        Label(root, text="Proceso completado. Nuevo archivo guardado.").pack()

# Crear la interfaz gráfica
root = Tk()
root.title("Procesar Excel")
root.geometry("300x100")

# Crear un botón para iniciar el proceso
Button(root, text="Iniciar", command=procesar_excel).pack(pady=20)

root.mainloop()
