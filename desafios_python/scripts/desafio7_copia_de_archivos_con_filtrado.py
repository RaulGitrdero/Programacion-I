import os
import re

while True:
    ruta_entrada = input("Nombre del archivo de origen: ").strip()
    try:
        with open(ruta_entrada, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        break
    except FileNotFoundError:
        print(f'No se encontró el archivo "{ruta_entrada}". Intenta de nuevo.')
    except (OSError, UnicodeDecodeError) as error:
        print(f"No se pudo leer el archivo: {error}")

while True:
    prohibida = input("Palabra prohibida: ").strip()
    if prohibida:
        break
    print("Debes escribir una palabra.")

while True:
    ruta_salida = input("Nombre del archivo de destino: ").strip()
    if not ruta_salida:
        print("Debes escribir un nombre de archivo.")
    elif os.path.abspath(ruta_salida) == os.path.abspath(ruta_entrada):
        print("El destino no puede ser el mismo archivo de origen.")
    else:
        break

patron = re.compile(rf"(?<!\w){re.escape(prohibida)}(?!\w)", re.IGNORECASE)
conservadas = [linea for linea in lineas if not patron.search(linea)]
omitidas = len(lineas) - len(conservadas)

try:
    with open(ruta_salida, "w", encoding="utf-8") as salida:
        salida.writelines(conservadas)
except OSError as error:
    print(f"No se pudo escribir el archivo de destino: {error}")
else:
    print(f"Líneas leídas: {len(lineas)}")
    print(f"Líneas copiadas: {len(conservadas)}")
    print(f'Líneas omitidas por contener "{prohibida}": {omitidas}')
    print(f'Resultado guardado en "{ruta_salida}".')
