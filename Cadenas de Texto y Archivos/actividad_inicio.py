"""Completa los TODO conforme a las reglas del documento Word."""
from pathlib import Path
from datetime import datetime
import json

BASE = Path(__file__).resolve().parent
ENTRADA = BASE / "datos" / "solicitudes.txt"
SALIDA = BASE / "salidas"

ENCABEZADO = "id|correo|categoria|descripcion"
CATALOGO = {"acceso", "pago_en_línea", "soporte_técnico"}
DIGITOS_ASCII = set("0123456789")

MOTIVOS = {
    "vacia": "línea vacía",
    "num_campos": "cantidad de campos distinta de cuatro",
    "campo_vacio": "campo vacío",
    "id": "ID con formato inválido",
    "correo": "correo inválido",
    "categoria": "categoría fuera del catálogo",
    "duplicado": "ID duplicado",
}

class EncabezadoInvalidoError(ValueError):
    pass

def normalizar_categoria(texto: str) -> str:
    # TODO: strip, lower, sustituir guiones/guiones bajos y unir palabras.
    t = texto.strip().lower().replace("-", " ").replace("_", " ")
    return "_".join(t.split())
    #raise NotImplementedError("Completa normalizar_categoria")

def normalizar_descripcion(texto):
    return " ".join(texto.split())

def id_valido(id_):
    return (len(id_) == 8 and id_.startswith("SOL-")
            and all(c in DIGITOS_ASCII for c in id_[4:]))


def correo_valido(correo):
    if correo.count("@") != 1 or any(c.isspace() for c in correo):
        return False
    usuario, dominio = correo.split("@")
    if not usuario or not dominio:
        return False
    return "." in dominio and not dominio.startswith(".") and not dominio.endswith(".")


def validar_campos(campos, ids_vistos):
    if len(campos) != 4:
        return None, MOTIVOS["num_campos"]
    if any(campo.strip() == "" for campo in campos):
        return None, MOTIVOS["campo_vacio"]

    id_ = campos[0].strip().upper()
    correo = campos[1].strip().lower()
    categoria = normalizar_categoria(campos[2])
    descripcion = normalizar_descripcion(campos[3])

    if not id_valido(id_):
        return None, MOTIVOS["id"]
    if not correo_valido(correo):
        return None, MOTIVOS["correo"]
    if categoria not in CATALOGO:
        return None, MOTIVOS["categoria"]
    if id_ in ids_vistos:
        return None, MOTIVOS["duplicado"]

    registro = {"id": id_, "correo": correo,
                "categoria": categoria, "descripcion": descripcion}
    return registro, None

def procesar(entrada, salida):
    with entrada.open("r", encoding="utf-8") as f_in:
        encabezado = f_in.readline().rstrip("\r\n")
        if encabezado != ENCABEZADO:
            raise EncabezadoInvalidoError(
                f"encabezado inesperado en {entrada.name}: {encabezado!r} "
                f"(se esperaba {ENCABEZADO!r}). No se modificaron las salidas.")

        salida.mkdir(parents=True, exist_ok=True)
        total = validos = rechazados = vacias = 0
        por_categoria = {}
        ids_vistos = set()
        lineas_rechazadas = []

        with (salida / "solicitudes_limpias.txt").open("w", encoding="utf-8") as f_ok, \
             (salida / "rechazos.jsonl").open("w", encoding="utf-8") as f_rej:
            f_ok.write(ENCABEZADO + "\n")

            for num_linea, linea in enumerate(f_in, start=2):
                total += 1
                original = linea.rstrip("\r\n")

                if original.strip() == "":
                    vacias += 1
                    registro, motivo = None, MOTIVOS["vacia"]
                else:
                    registro, motivo = validar_campos(original.split("|"), ids_vistos)

                if registro is None:
                    rechazados += 1
                    lineas_rechazadas.append(num_linea)
                    rechazo = {"linea": num_linea, "motivo": motivo,
                               "texto_original": original}
                    f_rej.write(json.dumps(rechazo, ensure_ascii=False) + "\n")
                else:
                    validos += 1
                    ids_vistos.add(registro["id"])
                    categoria = registro["categoria"]
                    por_categoria[categoria] = por_categoria.get(categoria, 0) + 1
                    f_ok.write("|".join(registro.values()) + "\n")

    resumen = {
        "total": total,
        "validos": validos,
        "rechazados": rechazados,
        "por_categoria": dict(sorted(por_categoria.items())),
        "lineas_vacias": vacias,
        "lineas_rechazadas": lineas_rechazadas,
        "tasa_aceptacion": round(validos / total, 4) if total else 0.0,
        "tasa_rechazo": round(rechazados / total, 4) if total else 0.0,
    }
    with (salida / "resumen.json").open("w", encoding="utf-8") as f_res:
        json.dump(resumen, f_res, ensure_ascii=False, indent=2)
    return resumen


def verificar_salidas(salida, esperado):
    with (salida / "solicitudes_limpias.txt").open("r", encoding="utf-8") as f:
        cabecera = f.readline().rstrip("\n")
        limpios = sum(1 for _ in f)

    with (salida / "resumen.json").open("r", encoding="utf-8") as f:
        resumen = json.load(f)

    rechazos = []
    with (salida / "rechazos.jsonl").open("r", encoding="utf-8") as f:
        for n, linea in enumerate(f, start=1):
            objeto = json.loads(linea)
            assert set(objeto) == {"linea", "motivo", "texto_original"}, \
                f"rechazos.jsonl, línea {n}: claves inesperadas"
            rechazos.append(objeto)

    assert cabecera == ENCABEZADO, "cabecera de solicitudes_limpias.txt incorrecta"
    assert limpios == esperado["validos"] == resumen["validos"], "conteo de válidos"
    assert len(rechazos) == esperado["rechazados"] == resumen["rechazados"], \
        "conteo de rechazados"
    assert resumen["total"] == resumen["validos"] + resumen["rechazados"], \
        "total != validos + rechazados"
    assert sum(resumen["por_categoria"].values()) == resumen["validos"], \
        "suma(por_categoria) != validos"
    assert [r["linea"] for r in rechazos] == resumen["lineas_rechazadas"], \
        "líneas rechazadas no coinciden"


def registrar_ejecucion(salida, entrada, resumen):
    marca = datetime.now().isoformat(timespec="seconds")
    with (salida / "ejecuciones.log").open("a", encoding="utf-8") as f:
        f.write(f"{marca} | entrada={entrada.name} | total={resumen['total']} "
                f"| validos={resumen['validos']} | rechazados={resumen['rechazados']}\n")


def main(entrada=ENTRADA, salida=SALIDA):
    try:
        resumen = procesar(entrada, salida)
        verificar_salidas(salida, resumen)
        registrar_ejecucion(salida, entrada, resumen)
    except FileNotFoundError as error:
        print(f"No se encontró el archivo de entrada: {error.filename}")
        return None
    except EncabezadoInvalidoError as error:
        print(f"Proceso detenido: {error}")
        return None

    print(f"Entrada: {entrada.name}")
    print(f"Total: {resumen['total']} | Válidos: {resumen['validos']} | "
          f"Rechazados: {resumen['rechazados']}")
    for categoria, cantidad in resumen["por_categoria"].items():
        print(f"  {categoria}: {cantidad}")
    print(f"Tasa de aceptación: {resumen['tasa_aceptacion']:.0%} | "
          f"Tasa de rechazo: {resumen['tasa_rechazo']:.0%}")
    print(f"Salidas verificadas en: {salida}")
    return resumen


if __name__ == "__main__":
    main()
