import re
import networkx as nx
import matplotlib.pyplot as plt

def es_expresion_regular_valida(expresion):
    def validar_expresion(expresion):
        stack = []

        for char in expresion:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False

        return len(stack) == 0

    if validar_expresion(expresion):
        i = 0
        while i < len(expresion):
            char = expresion[i]
            if char == '*' or char == '|' or char == '.':
                if i == 0 or i == len(expresion) - 1:
                    return False
                prev_char = expresion[i - 1]
                next_char = expresion[i + 1]
                if prev_char in ['*', '|', '.'] or next_char in ['*', '|', '.']:
                    return False
            i += 1
        return True
    else:
        return False

# Test cases
def iniciar():
    #expresion = input("Ingrese una expresión regular (con a-z, A-Z, 0-9, ., |, *, (, ), ε, ∼, Φ): ")
    expresion = "a*"
    if es_expresion_regular_valida(expresion):
        print("La expresión regular es válida.")

        #testAFNDToAFD()
        
        
    else:
        print("La expresión regular no es válida.")
iniciar()
