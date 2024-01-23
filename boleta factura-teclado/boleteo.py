# boleteo.py
import pyautogui
import time
import pandas as pd

def ejecutar_codigo(datos_para_insertar):
    # Coordenadas de la consola
    x_clic_adicional_1 = 955
    y_clic_adicional_1 = 290

    
    pyautogui.click(x_clic_adicional_1, y_clic_adicional_1, duration=1)

    pyautogui.press('tab')      
    pyautogui.press('tab')
    for datos in datos_para_insertar:

        if datos["IGV"] == 'no':
                precio_unitario_ajustado = datos["precio"]
        else:
                precio_unitario_ajustado = round(datos["precio"] / 1.18, 10)
        
        # Presiona la tecla Tab
        pyautogui.press('enter')
        time.sleep(2)

        pyautogui.press('right')
        # pyautogui.click(x_clic_adicional_2, y_clic_adicional_2, duration=1)
        pyautogui.press('tab') 
        pyautogui.press('1')

        pyautogui.press('tab') 
        pyautogui.write(datos["nombre"])

        pyautogui.press('tab') 
        pyautogui.press('tab') 
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write(str(precio_unitario_ajustado))

        pyautogui.press('tab')
        pyautogui.press('tab')

        if datos["IGV"] == 'no':
                pyautogui.press('right')
        
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')


        pyautogui.write(datos["unidad"])

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(2)

def leer_excel(nombre_archivo):
    try:
        # Lee el archivo Excel
        datos = pd.read_excel(nombre_archivo)
        return datos
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return None

def actualizar_tabla(tabla, datos):
    # Limpia la tabla existente
    for row in tabla.get_children():
        tabla.delete(row)

    # Llena la tabla con los nuevos datos del DataFrame
    for fila in datos.itertuples(index=False):
        valores_fila = tuple(fila) + (fila.precio / 1.18, fila.precio * fila.unidad)
        tabla.insert("", "end", values=valores_fila)

def iniciar_boleteo(tabla, ventana_resultado):
    # Obtén los datos actuales de la tabla
    datos_actuales = []
    for item_id in tabla.get_children():
        datos = [tabla.item(item_id, 'values')[i] for i in range(4)]
        datos_actuales.append({'unidad': datos[0], 'nombre': datos[1], 'precio': float(datos[2]), 'IGV': datos[3]})

    # Llama a la función ejecutar_codigo con los datos actuales
    ejecutar_codigo(datos_actuales)

    # Muestra la ventana de resultado
    ventana_resultado.deiconify()