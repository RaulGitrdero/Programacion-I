import re
from collections import Counter

while True:
    ruta_entrada = input("Nombre del archivo de texto a analizar: ").strip()
    try:
        with open(ruta_entrada, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
        break
    except FileNotFoundError:
        print(f'No se encontró el archivo "{ruta_entrada}". Intenta de nuevo.')
    except (OSError, UnicodeDecodeError) as error:
        print(f"No se pudo leer el archivo: {error}")

palabras = re.findall(r"[^\W\d_]+", texto.lower())

if not palabras:
    print("El archivo no contiene palabras.")
else:
    conteo = Counter(palabras)
    ordenadas = sorted(conteo.items(), key=lambda par: (-par[1], par[0]))
    ruta_salida = "estadisticas_palabras.txt"

    with open(ruta_salida, "w", encoding="utf-8") as salida:
        salida.write(f"Total de palabras: {len(palabras)}\n")
        salida.write(f"Palabras distintas: {len(conteo)}\n\n")
        for palabra, veces in ordenadas:
            salida.write(f"{palabra}: {veces}\n")

    print(f"Total de palabras: {len(palabras)}")
    print(f"Palabras distintas: {len(conteo)}")
    print("\nLas 10 más frecuentes:")
    for palabra, veces in ordenadas[:10]:
        print(f"  {palabra}: {veces}")
    print(f'\nEstadísticas completas guardadas en "{ruta_salida}".')
