import tkinter as tk
from tkinter import ttk, messagebox


class CalculadoraDarkApp:
    # Paleta de colores (Dark Modern Theme)
    BG_PRINCIPAL = "#0f172a"      # Azul marino muy oscuro
    BG_TARJETA = "#1e293b"        # Azul pizarra intermedio
    BG_INPUT = "#334155"          # Fondo para inputs
    TEXT_BLANCO = "#ffffff"       # Texto blanco para etiquetas
    TEXT_SUAVE = "#94a3b8"        # Texto secundario
    COLOR_MENTA = "#4ade80"       # Verde menta para resultados
    COLOR_BOTON_CALCULAR = "#ef4444"  # Rojo para botón calcular
    COLOR_BOTON_LIMPIAR = "#22c55e"   # Verde para botón limpiar
    TEXT_OSCURO = "#0f172a"       # Texto oscuro para contrastar con colores claros

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Calculadora - Dark Mode")
        self.root.geometry("620x360")
        self.root.resizable(False, False)
        self.root.configure(bg=self.BG_PRINCIPAL)

        # Variables de control
        self.num1_var = tk.StringVar()
        self.operacion_var = tk.StringVar(value="Sumar")
        self.num2_var = tk.StringVar()
        self.resultado_var = tk.StringVar(value="Resultado: —")

        self._configurar_estilos()
        self._construir_interfaz()

    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Configuración visual del Combobox para integrarse al modo oscuro
        self.style.configure(
            "Dark.TCombobox",
            fieldbackground=self.BG_INPUT,
            background=self.BG_TARJETA,
            foreground=self.TEXT_BLANCO,
            arrowcolor=self.COLOR_MENTA,
            bordercolor=self.BG_INPUT,
            lightcolor=self.BG_INPUT,
            darkcolor=self.BG_INPUT,
            padding=6
        )
        self.style.map(
            "Dark.TCombobox",
            fieldbackground=[("readonly", self.BG_INPUT)],
            foreground=[("readonly", self.TEXT_BLANCO)]
        )

    def _construir_interfaz(self):
        # Contenedor central (tarjeta) con margen
        tarjeta = tk.Frame(
            self.root,
            bg=self.BG_TARJETA,
            padx=25,
            pady=25,
            highlightbackground="#334155",
            highlightthickness=1
        )
        tarjeta.pack(fill="both", expand=True, padx=25, pady=25)

        # --- ESTRUCTURA SUPERIOR: 3 campos en línea horizontal ---
        frame_superior = tk.Frame(tarjeta, bg=self.BG_TARJETA)
        frame_superior.pack(fill="x", pady=(0, 20))

        frame_superior.columnconfigure(0, weight=1)
        frame_superior.columnconfigure(1, weight=1)
        frame_superior.columnconfigure(2, weight=1)

        # Campo 1: Primer número
        f_num1 = tk.Frame(frame_superior, bg=self.BG_TARJETA)
        f_num1.grid(row=0, column=0, padx=8, sticky="ew")

        tk.Label(
            f_num1,
            text="Primer número",
            font=("Segoe UI", 10, "bold"),
            fg=self.TEXT_BLANCO,
            bg=self.BG_TARJETA
        ).pack(anchor="w", pady=(0, 6))

        self.entry_num1 = tk.Entry(
            f_num1,
            textvariable=self.num1_var,
            font=("Segoe UI", 11),
            bg=self.BG_INPUT,
            fg=self.TEXT_BLANCO,
            insertbackground=self.COLOR_MENTA,
            relief="flat",
            justify="center",
            highlightthickness=1,
            highlightbackground="#475569",
            highlightcolor=self.COLOR_MENTA
        )
        self.entry_num1.pack(fill="x", ipady=6)
        self.entry_num1.focus_set()

        # Campo 2: Operación
        f_op = tk.Frame(frame_superior, bg=self.BG_TARJETA)
        f_op.grid(row=0, column=1, padx=8, sticky="ew")

        tk.Label(
            f_op,
            text="Operación",
            font=("Segoe UI", 10, "bold"),
            fg=self.TEXT_BLANCO,
            bg=self.BG_TARJETA
        ).pack(anchor="w", pady=(0, 6))

        self.combo_op = ttk.Combobox(
            f_op,
            textvariable=self.operacion_var,
            values=["Sumar", "Restar", "Multiplicar", "Dividir"],
            state="readonly",
            style="Dark.TCombobox",
            font=("Segoe UI", 10),
            justify="center"
        )
        self.combo_op.pack(fill="x", ipady=4)

        # Campo 3: Segundo número
        f_num2 = tk.Frame(frame_superior, bg=self.BG_TARJETA)
        f_num2.grid(row=0, column=2, padx=8, sticky="ew")

        tk.Label(
            f_num2,
            text="Segundo número",
            font=("Segoe UI", 10, "bold"),
            fg=self.TEXT_BLANCO,
            bg=self.BG_TARJETA
        ).pack(anchor="w", pady=(0, 6))

        self.entry_num2 = tk.Entry(
            f_num2,
            textvariable=self.num2_var,
            font=("Segoe UI", 11),
            bg=self.BG_INPUT,
            fg=self.TEXT_BLANCO,
            insertbackground=self.COLOR_MENTA,
            relief="flat",
            justify="center",
            highlightthickness=1,
            highlightbackground="#475569",
            highlightcolor=self.COLOR_MENTA
        )
        self.entry_num2.pack(fill="x", ipady=6)

        # --- BOTONES DE ACCIÓN ---
        frame_botones = tk.Frame(tarjeta, bg=self.BG_TARJETA)
        frame_botones.pack(pady=(5, 20))

        # Botón Calcular (rojo con texto blanco)
        self.btn_calcular = tk.Button(
            frame_botones,
            text="Calcular",
            command=self.calcular,
            font=("Segoe UI", 11, "bold"),
            bg=self.COLOR_BOTON_CALCULAR,
            fg=self.TEXT_BLANCO,
            activebackground="#dc2626",
            activeforeground=self.TEXT_BLANCO,
            relief="flat",
            cursor="hand2",
            padx=24,
            pady=8,
            highlightthickness=2,
            highlightbackground=self.BG_TARJETA,
            highlightcolor="#ffffff"
        )
        self.btn_calcular.pack(side="left", padx=10)
        self.btn_calcular.bind("<Return>", lambda event: self.calcular())

        # Botón Limpiar (verde con texto blanco)
        self.btn_limpiar = tk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar,
            font=("Segoe UI", 11, "bold"),
            bg=self.COLOR_BOTON_LIMPIAR,
            fg=self.TEXT_BLANCO,
            activebackground="#16a34a",
            activeforeground=self.TEXT_BLANCO,
            relief="flat",
            cursor="hand2",
            padx=24,
            pady=8,
            highlightthickness=2,
            highlightbackground=self.BG_TARJETA,
            highlightcolor="#ffffff"
        )
        self.btn_limpiar.pack(side="left", padx=10)
        self.btn_limpiar.bind("<Return>", lambda event: self.limpiar())

        # Permitir calcular al presionar Enter en los campos de texto
        self.entry_num1.bind("<Return>", lambda event: self.calcular())
        self.entry_num2.bind("<Return>", lambda event: self.calcular())

        # --- RESULTADO INFERIOR ---
        lbl_resultado = tk.Label(
            tarjeta,
            textvariable=self.resultado_var,
            font=("Segoe UI", 16, "bold"),
            fg=self.COLOR_MENTA,
            bg=self.BG_TARJETA
        )
        lbl_resultado.pack(pady=(5, 5))

    def limpiar(self, event=None):
        """Borra el contenido de los dos campos y restablece el resultado."""
        self.num1_var.set("")
        self.num2_var.set("")
        self.operacion_var.set("Sumar")
        self.resultado_var.set("Resultado: —")
        self.entry_num1.focus_set()

    def calcular(self, event=None):
        """Valida entradas y calcula el resultado."""
        str_n1 = self.num1_var.get().strip()
        str_n2 = self.num2_var.get().strip()

        # Validación de campos no vacíos
        if not str_n1 or not str_n2:
            messagebox.showwarning("Campos incompletos", "Por favor ingresa ambos números.")
            if not str_n1:
                self.entry_num1.focus_set()
            else:
                self.entry_num2.focus_set()
            return

        # Validación de tipos numéricos
        try:
            n1 = float(str_n1)
        except ValueError:
            messagebox.showerror("Dato no válido", f"'{str_n1}' no es un número válido.")
            self.entry_num1.focus_set()
            return

        try:
            n2 = float(str_n2)
        except ValueError:
            messagebox.showerror("Dato no válido", f"'{str_n2}' no es un número válido.")
            self.entry_num2.focus_set()
            return

        operacion = self.operacion_var.get()

        # Lógica de cálculo y validación de división por cero
        if operacion == "Sumar":
            res = n1 + n2
        elif operacion == "Restar":
            res = n1 - n2
        elif operacion == "Multiplicar":
            res = n1 * n2
        elif operacion == "Dividir":
            if n2 == 0:
                signo = "-" if n1 < 0 else ""
                self.resultado_var.set(f"Resultado: {signo}∞ (Infinito)")
                return
            res = n1 / n2
        else:
            messagebox.showerror("Error", "Operación no reconocida.")
            return

        # Mostrar resultado formateado
        res_formateado = f"{res:g}"
        self.resultado_var.set(f"Resultado: {res_formateado}")


def main():
    root = tk.Tk()
    app = CalculadoraDarkApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
