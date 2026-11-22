def componer(funciones):
    funciones = list(funciones)
    if not funciones:
        raise ValueError("Se necesita al menos una función para componer.")
    for funcion in funciones:
        if not callable(funcion):
            raise TypeError("Todos los elementos de la lista deben ser funciones.")

    def compuesta(*args, **kwargs):
        resultado = funciones[0](*args, **kwargs)
        for funcion in funciones[1:]:
            resultado = funcion(resultado)
        return resultado

    return compuesta


if __name__ == "__main__":
    def sumar_uno(x):
        return x + 1


    def duplicar(x):
        return x * 2


    def al_cuadrado(x):
        return x ** 2


    f = componer([sumar_uno, duplicar, al_cuadrado])
    print("f(3) = ((3 + 1) * 2) ** 2 =", f(3))

    g = componer([str.strip, str.upper, lambda texto: texto + "!"])
    print("g('  hola mundo  ') =", g("  hola mundo  "))

    h = componer([len, sumar_uno, duplicar])
    print("h('abc') = (len('abc') + 1) * 2 =", h("abc"))

    solo_una = componer([al_cuadrado])
    print("Composición de una sola función, solo_una(7) =", solo_una(7))

    primera_con_varios_argumentos = componer([max, al_cuadrado])
    print("max(2, 9, 4) al cuadrado =", primera_con_varios_argumentos(2, 9, 4))

    print("\nCasos de error:")
    for descripcion, llamada in [
        ("lista vacía", lambda: componer([])),
        ("elemento que no es función", lambda: componer([sumar_uno, 5])),
    ]:
        try:
            llamada()
        except (TypeError, ValueError) as error:
            print(f"{descripcion}: {type(error).__name__} - {error}")
