import datetime
import locale

# Configura la localización en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Define la fecha del 1 de febrero de 2024
fecha = datetime.datetime(2024, 2, 1)

# Obtiene el nombre del día de la semana en español y lo convierte a mayúsculas
nombre_dia = fecha.strftime('%A').upper()

# Obtiene el número del día del mes
numero_dia = fecha.day

# Imprime el nombre del día de la semana y el número del día en mayúsculas
print(nombre_dia, numero_dia)
