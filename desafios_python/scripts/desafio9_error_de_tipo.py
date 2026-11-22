def concatenate_list_of_strings_original(string_list):
    concatenated_string = ""
    for item in string_list:
        concatenated_string += item
    return concatenated_string


def concatenate_list_of_strings(string_list):
    if isinstance(string_list, (str, bytes)) or not hasattr(string_list, "__iter__"):
        raise TypeError("Se esperaba una lista de elementos.")
    return "".join(str(item) for item in string_list)


if __name__ == "__main__":
    mixed_list = ["hello", "world", 123, True, "!", 42.0]

    try:
        result = concatenate_list_of_strings_original(mixed_list)
        print("Concatenated Result (original):", result)
    except TypeError as e:
        print("TypeError (original):", e)

    try:
        result = concatenate_list_of_strings(mixed_list)
        print("Concatenated Result (corregida):", result)
    except TypeError as e:
        print("TypeError:", e)

    casos = [[], ["a", "b"], [1, 2, 3], [None, [1, 2], {"k": 1}], ("x", 5)]
    print("\nMás casos de prueba:")
    for caso in casos:
        print(f"{caso!r} -> {concatenate_list_of_strings(caso)!r}")

    print("\nEntradas inválidas:")
    for entrada in ["texto", 123]:
        try:
            concatenate_list_of_strings(entrada)
        except TypeError as e:
            print(f"{entrada!r}: TypeError - {e}")
