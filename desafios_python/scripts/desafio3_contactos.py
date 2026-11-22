import re

contactos = []


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo no puede estar vacío.")


def pedir_telefono():
    while True:
        telefono = input("Teléfono: ").strip()
        digitos = re.sub(r"[\s\-()+]", "", telefono)
        if digitos.isdigit() and 7 <= len(digitos) <= 15:
            return telefono
        print("Teléfono inválido. Usa de 7 a 15 dígitos (se permiten espacios, guiones, paréntesis y +).")


def pedir_correo():
    while True:
        correo = input("Correo electrónico: ").strip()
        if re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", correo):
            return correo
        print("Correo inválido. Ejemplo: nombre@dominio.com")


def indice_de_contacto(nombre):
    for i, (nombre_guardado, _) in enumerate(contactos):
        if nombre_guardado.lower() == nombre.lower():
            return i
    return -1


def mostrar_contacto(nombre, info):
    print(f"  Nombre:   {nombre}")
    print(f"  Teléfono: {info['telefono']}")
    print(f"  Correo:   {info['correo']}")


def agregar_contacto():
    nombre = pedir_texto("Nombre: ")
    if indice_de_contacto(nombre) != -1:
        print(f'Ya existe un contacto llamado "{nombre}".')
        return
    info = {"telefono": pedir_telefono(), "correo": pedir_correo()}
    contactos.append((nombre, info))
    print(f'Contacto "{nombre}" agregado.')


def ver_contactos():
    if not contactos:
        print("La lista de contactos está vacía.")
        return
    print(f"\nContactos ({len(contactos)}):")
    for numero, (nombre, info) in enumerate(contactos, start=1):
        print(f"{numero}.")
        mostrar_contacto(nombre, info)


def buscar_contacto():
    consulta = pedir_texto("Nombre a buscar: ").lower()
    encontrados = [(nombre, info) for nombre, info in contactos if consulta in nombre.lower()]
    if not encontrados:
        print("No se encontraron contactos con ese nombre.")
        return
    print(f"\nResultados ({len(encontrados)}):")
    for nombre, info in encontrados:
        mostrar_contacto(nombre, info)


def eliminar_contacto():
    nombre = pedir_texto("Nombre a eliminar: ")
    indice = indice_de_contacto(nombre)
    if indice == -1:
        print("No existe un contacto con ese nombre.")
        return
    eliminado = contactos.pop(indice)
    print(f'Contacto "{eliminado[0]}" eliminado.')


def menu():
    acciones = {
        "1": agregar_contacto,
        "2": ver_contactos,
        "3": buscar_contacto,
        "4": eliminar_contacto,
    }
    while True:
        print("\n--- Administrador de contactos ---")
        print("1. Agregar un contacto nuevo")
        print("2. Ver la lista de contactos")
        print("3. Buscar un contacto por nombre")
        print("4. Eliminar un contacto por nombre")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "5":
            print("Hasta luego.")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida, elige un número del 1 al 5.")
        else:
            accion()


if __name__ == "__main__":
    menu()
