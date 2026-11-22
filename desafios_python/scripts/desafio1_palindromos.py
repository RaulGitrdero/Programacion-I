import unicodedata

while True:
    texto = input("Ingresa una palabra o frase: ")
    limpio = unicodedata.normalize("NFD", texto.lower())
    limpio = "".join(c for c in limpio if unicodedata.category(c) != "Mn")
    limpio = "".join(c for c in limpio if c.isalnum())
    if limpio:
        break
    print("No ingresaste letras ni números, intenta de nuevo.")

if limpio == limpio[::-1]:
    print(f'"{texto}" SÍ es un palíndromo.')
else:
    print(f'"{texto}" NO es un palíndromo.')
