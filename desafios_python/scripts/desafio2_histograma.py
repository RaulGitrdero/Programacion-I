conteo = {}

while not conteo:
    texto = input("Ingresa letras, números o ambos: ")
    for caracter in texto.lower():
        if caracter.isalnum():
            conteo[caracter] = conteo.get(caracter, 0) + 1
    if not conteo:
        print("No ingresaste letras ni números, intenta de nuevo.")

print("\nHistograma de caracteres:")
for caracter in sorted(conteo):
    print(f"{caracter} | {'*' * conteo[caracter]} ({conteo[caracter]})")
