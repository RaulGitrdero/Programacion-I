def sort_list_bad(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
    return numbers


def sort_list(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Se esperaba una lista de números.")
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


if __name__ == "__main__":
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    print("Lista original:       ", test_list)
    print("Resultado con error:  ", sort_list_bad(test_list.copy()))
    print("Resultado corregido:  ", sort_list(test_list.copy()))
    print("Coincide con sorted():", sort_list(test_list.copy()) == sorted(test_list))

    casos = [[], [1], [2, 1], [1, 2, 3], [5, 4, 3, 2, 1], [-3, 0, -1, 7, 7], [2.5, 1.5, 3]]
    print("\nMás casos de prueba:")
    for caso in casos:
        ordenada = sort_list(caso.copy())
        print(f"{caso} -> {ordenada}  correcto: {ordenada == sorted(caso)}")

    try:
        sort_list("321")
    except TypeError as error:
        print("\nEntrada inválida:", error)
