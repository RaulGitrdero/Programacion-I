# Programación I

**Maestría en Ciencia de Datos (MCD) · CUCEA, Universidad de Guadalajara**
**Autor:** Raúl Cordero

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-GitHub-181717?logo=github&logoColor=white)

Bienvenido al repositorio de la asignatura **Programación I**, correspondiente a la Maestría en Ciencia de Datos. Este espacio reúne los materiales, ejercicios y proyectos orientados al aprendizaje del lenguaje Python y al desarrollo de soluciones computacionales aplicadas al análisis de datos.

Durante el curso se abordan los fundamentos de programación, el manejo de variables y estructuras de control, la manipulación de cadenas y archivos, las estructuras de datos, la programación orientada a objetos, las expresiones regulares, los servicios web y la integración con bases de datos SQL. Asimismo, se utilizan herramientas para la depuración y prueba de programas, así como Git y GitHub para el control de versiones y el desarrollo colaborativo.

---

## Objetivo

Desarrollar las habilidades necesarias para **diseñar, implementar, depurar y documentar** programas en Python, integrando buenas prácticas de programación y herramientas de colaboración.

## Contenido general

| # | Tema | Conceptos clave |
|---|------|-----------------|
| 1 | Arquitectura y fundamentos de Python | Intérprete, ejecución de scripts y notebooks, sintaxis básica |
| 2 | Variables, tipos de datos y estructuras de control | Tipos primitivos, conversiones, `if`, `for`, `while` |
| 3 | Manipulación de cadenas | Métodos de `str`, slicing, f-strings, Unicode |
| 4 | Lectura y escritura de archivos | `open()`, `with`, codificación UTF-8, manejo de errores |
| 5 | Estructuras de datos | Listas, tuplas, diccionarios, conjuntos, comprensiones |
| 6 | Expresiones regulares | Módulo `re`, patrones, búsqueda, validación y sustitución |
| 7 | Programación orientada a objetos | Clases, objetos, herencia, encapsulamiento |
| 8 | Sockets y servicios web | Comunicación en red, HTTP, consumo de APIs |
| 9 | Bases de datos SQL | Conexión desde Python, consultas, ORM |
| 10 | Depuración y pruebas de código | Depuradores, casos de prueba, pruebas unitarias |
| 11 | Control de versiones con Git y GitHub | Commits, ramas, repositorios remotos, colaboración |

---

## Actividades del curso

| Actividad | Descripción | Temas aplicados |
|-----------|-------------|-----------------|
| [Desafíos de Programación 1](./desafios-python) | 9 desafíos resueltos como scripts y en un notebook, con código comentado y una visualización de la ejecución paso a paso | Cadenas, archivos, estructuras de datos, funciones, expresiones regulares, depuración |

*En este repositorio se irán publicando ejemplos, prácticas, actividades y proyectos conforme avance el curso.*

## Estructura del repositorio

```
Programacion-I/
├── README.md                 Este documento
└── desafios-python/          Desafíos de Programación 1
    ├── README.md             Descripción detallada de cada desafío
    ├── desafios_python_completo.ipynb
    ├── scripts/              Un script .py por desafío
    ├── archivos_texto/       Archivos de entrada de los desafíos 6 y 7
    └── visualizacion/        Animación de la ejecución línea por línea
```

Cada actividad tiene su propia carpeta y su propio README con el enunciado, la explicación de la solución y las instrucciones de ejecución.

---

## Requisitos

- **Python 3.8 o superior.**
- **Jupyter** (Notebook, JupyterLab o VS Code con la extensión de Jupyter) para abrir los notebooks.
- **Git** para clonar el repositorio.

Salvo que una actividad indique lo contrario, solo se usa la biblioteca estándar de Python.

## Cómo usar este repositorio

```bash
git clone https://github.com/<usuario>/Programacion-I.git
cd Programacion-I/desafios-python
python scripts/desafio1_palindromos.py
```

Para los notebooks, abre el archivo `.ipynb` en Jupyter y ejecuta las celdas de arriba hacia abajo.

## Metodología de trabajo

Cada actividad sigue el mismo proceso:

1. **Estudio del problema:** entender qué se pide antes de escribir código.
2. **Diseño:** dividir la solución en partes pequeñas.
3. **Codificación:** implementar una solución funcional.
4. **Depuración:** probar con casos normales, casos límite y entradas inválidas.
5. **Optimización:** mejorar la eficiencia y la legibilidad.
6. **Documentación:** comentarios en el código y un README por actividad.
7. **Publicación:** subir la solución a este repositorio con Git.

## Herramientas

- **Lenguaje:** Python
- **Entornos:** Jupyter Notebook, VS Code
- **Control de versiones:** Git y GitHub

---

**Raúl Cordero** · Maestría en Ciencia de Datos · CUCEA, Universidad de Guadalajara
