import re

class NumeroAutomata:
    def __init__(self):
        self.regex_entero = re.compile(r'^-?\d+$')
        self.regex_flotante = re.compile(r'^-?\d+(\.\d+)?(e[-+]?\d+)?$')
        self.regex_hexadecimal = re.compile(r'^-?0x[0-9a-fA-F]+$')

    def es_entero(self, cadena):
        return bool(self.regex_entero.match(cadena))

    def es_flotante(self, cadena):
        return bool(self.regex_flotante.match(cadena))

    def es_hexadecimal(self, cadena):
        return bool(self.regex_hexadecimal.match(cadena))

automata = NumeroAutomata()

while True:
    print("Ingrese un numero para reconocer...")
    caso = input().strip()
    if automata.es_entero(caso):
        print(f"{caso} es un número entero.")
    elif automata.es_flotante(caso):
        print(f"{caso} es un número flotante.")
    elif automata.es_hexadecimal(caso):
        print(f"{caso} es un número hexadecimal.")
    else:
        print(f"{caso} no es reconocido por el autómata.")