import re

class Automata:
    def __init__(self):
        self.entero = re.compile(r'^-?\d+$')
        self.flotante = re.compile(r'^-?\d+(\.\d+)?(e[-+]?\d+)?$')
        self.hexadecimal = re.compile(r'^-?0x[0-9a-fA-F]+$')

    def Esentero(self, cadena):
        return bool(self.entero.match(cadena))

    def Esflotante(self, cadena):
        return bool(self.flotante.match(cadena))

    def Eshexadecimal(self, cadena):
        return bool(self.hexadecimal.match(cadena))

automata = Automata()

while True:
    print("Ingrese un numero para reconocer...")
    caso = input().strip()
    if automata.Esentero(caso):
        print(f"{caso} es un número entero.")
    elif automata.Esflotante(caso):
        print(f"{caso} es un número flotante.")
    elif automata.Eshexadecimal(caso):
        print(f"{caso} es un número hexadecimal.")
    else:
        print(f"{caso} no es reconocido por el autómata.")