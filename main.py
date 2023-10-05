import re

def validar_expresion_regular(expresion):
    try:
        re.compile(expresion)
        return True
    except re.error:
        return False

expresion = input("Ingrese una expresión regular (con a-z, A-Z, 0-9, ., |, *, (, ), ε, ∼, Φ): ")

if validar_expresion_regular(expresion):
    print("La expresión regular es válida.")
else:
    print("La expresión regular no es válida.")
