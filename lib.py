# lib.py

if __name__ == '__main__':
    print('holi')

# Generamos una funcion para corregir los nombres de las lineas
def fix_linea(dato):
    """La funcion lee las lineas y corrgie los casos donde hay un acento para unificarlo en modalidad sin acentos"""
    if dato == "Línea 1":
        return "Linea 1"
    elif dato == "Línea 2":
        return "Linea 2"
    elif dato == "Línea 3":
        return "Linea 3"
    elif dato == "Línea 4":
        return "Linea 4"
    elif dato == "Línea 5":
        return "Linea 5"
    elif dato == "Línea 6":
        return "Linea 6"
    elif dato == "Línea 7":
        return "Linea 7"
    elif dato == "Línea 8":
        return "Linea 8"
    elif dato == "Línea 9":
        return "Linea 9"
    elif dato == "Línea A":
        return "Linea A"
    elif dato == "Línea B":
        return "Linea B"
    elif dato == "Línea 12":
        return "Linea 12"
    else:
        return dato

# Diseñamos una formula para rellenar los datos perdidos de la columna mes
def fill_mes(dato):
    """La funcion recibe un numero de mes y devuelve el nombre del mes"""
    if dato == 12:
        return "Diciembre"
    elif dato == 11:
        return "Noviembre"
    elif dato == 10:
        return "Octubre"
    elif dato == 9:
        return "Septiembre"
    elif dato == 8:
        return "Agosto"
    elif dato == 7:
        return "Julio"
    elif dato == 6:
        return "Junio"
    elif dato == 5:
        return "Mayo"
    elif dato == 4:
        return "Abril"
    elif dato == 3:
        return "Marzo"
    elif dato == 2:
        return "Febrero"
    elif dato == 1:
        return "Enero"
