SIN_VALOR = object()


def verificar_funcion(funcion):
    if not callable(funcion):
        raise TypeError("El primer argumento debe ser una función.")


def mi_map(funcion, lista):
    verificar_funcion(funcion)
    resultado = []
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado


def mi_filter(funcion, lista):
    verificar_funcion(funcion)
    resultado = []
    for elemento in lista:
        if funcion(elemento):
            resultado.append(elemento)
    return resultado


def mi_reduce(funcion, lista, inicial=SIN_VALOR):
    verificar_funcion(funcion)
    iterador = iter(lista)
    if inicial is SIN_VALOR:
        try:
            acumulado = next(iterador)
        except StopIteration:
            raise TypeError("mi_reduce() con una lista vacía requiere un valor inicial.") from None
    else:
        acumulado = inicial
    for elemento in iterador:
        acumulado = funcion(acumulado, elemento)
    return acumulado


if __name__ == "__main__":
    from functools import reduce

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    palabras = ["python", "spark", "pandas", "sql"]

    cuadrados = mi_map(lambda x: x ** 2, numeros)
    pares = mi_filter(lambda x: x % 2 == 0, numeros)
    suma = mi_reduce(lambda acumulado, x: acumulado + x, numeros)
    producto = mi_reduce(lambda acumulado, x: acumulado * x, numeros, 1)
    mayusculas = mi_map(str.upper, palabras)
    largas = mi_filter(lambda p: len(p) > 5, palabras)
    frase = mi_reduce(lambda acumulado, p: acumulado + " " + p, palabras, "Herramientas:")

    print("Cuadrados:", cuadrados)
    print("Pares:", pares)
    print("Suma:", suma)
    print("Producto:", producto)
    print("Mayúsculas:", mayusculas)
    print("Palabras de más de 5 letras:", largas)
    print("Frase:", frase)

    print("\nComparación con las funciones originales de Python:")
    print("mi_map == map:", cuadrados == list(map(lambda x: x ** 2, numeros)))
    print("mi_filter == filter:", pares == list(filter(lambda x: x % 2 == 0, numeros)))
    print("mi_reduce == reduce:", suma == reduce(lambda a, x: a + x, numeros))
    print("mi_reduce con inicial == reduce:", producto == reduce(lambda a, x: a * x, numeros, 1))
    print("Lista vacía con inicial:", mi_reduce(lambda a, x: a + x, [], 0))

    print("\nCasos de error:")
    for descripcion, llamada in [
        ("lista vacía sin inicial", lambda: mi_reduce(lambda a, x: a + x, [])),
        ("primer argumento no es función", lambda: mi_map(5, numeros)),
    ]:
        try:
            llamada()
        except TypeError as error:
            print(f"{descripcion}: TypeError - {error}")
