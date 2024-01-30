import re
import tkinter as tk
from tkinter import messagebox

class NumeroReconocedor:
    def __init__(self):
        self.patron = r'^(\+|-)?(0x[a-fA-F0-9]+|(\d+(\.\d+)?([eE](\+|-)?\d+)?))$'

    def es_valido(self, numero):
        return re.match(self.patron, numero) is not None

class Aplicacion:
    def __init__(self, root):
        self.root = root
        root.title("Reconocedor de Números")

        self.reconocedor = NumeroReconocedor()

        self.label = tk.Label(root, text="Introduce un número:")
        self.label.pack()

        self.entrada = tk.Entry(root)
        self.entrada.pack()

        self.boton = tk.Button(root, text="Verificar", command=self.verificar)
        self.boton.pack()

    def verificar(self):
        numero = self.entrada.get()
        if self.reconocedor.es_valido(numero):
            messagebox.showinfo("Resultado", f"'{numero}' es un número válido.")
        else:
            messagebox.showwarning("Resultado", f"'{numero}' no es un número válido.")

root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
