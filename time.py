from datetime import datetime

# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Convertir la fecha a un string en el formato deseado (solo día, mes y año)
fecha_string = fecha_actual.strftime("%d-%m-%Y")

# Imprimir la fecha como string
print("La fecha actual es:", fecha_string)

# O simplemente asignarla a una variable
# fecha_string = fecha_actual.strftime("%d-%m-%Y")
