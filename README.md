# Calculadora Dark Mode (Python Tkinter)

Aplicación de escritorio moderna desarrollada en Python utilizando `tkinter` y `ttk`, con una interfaz gráfica en modo oscuro (Dark Mode).

## Características

- **Diseño Moderno Oscuro**: Paleta de colores basada en tonos azul marino (`#0f172a`), pizarra y acentos verde menta (`#4ade80`).
- **Disposición Horizontal**: Entradas para el primer número, selector de operación y segundo número organizados de forma clara en una fila.
- **Operaciones Aritméticas**:
  - Suma (+)
  - Resta (-)
  - Multiplicación (×)
  - División (÷) mostrando Infinito (∞) al dividir por cero.
- **Acciones Rápidas y Accesibilidad**:
  - Botón **Calcular** (rojo) para procesar los datos (soporta ejecución directa con la tecla `Enter`).
  - Botón **Limpiar** (verde) para restablecer los campos y el resultado (soporta la tecla `Enter`).
- **Validación de Entradas**: Detección de campos vacíos o valores no numéricos.

## Requisitos

- Python 3.8 o superior.
- No requiere librerías externas (utiliza la librería estándar `tkinter`).

## Ejecución

Para iniciar la aplicación:

```bash
python main.py
```
*(En Windows también puedes usar `py main.py`)*

## Compilar a `.exe` (Opcional)

Si deseas empaquetar la aplicación en un ejecutable independiente de Windows:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name "Calculadora" main.py
```
El archivo `.exe` se generará en la carpeta `dist/`.

