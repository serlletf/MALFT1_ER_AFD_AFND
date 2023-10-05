import re
import networkx as nx

def validar_expresion_regular(expresion):
    try:
        re.compile(expresion)
        return True
    except re.error:
        return False

def construir_AFND(expresion):
    grafo = nx.DiGraph()
    pila = []

    for caracter in expresion:
        if caracter == '(':
            pila.append(grafo.copy())
            grafo = nx.DiGraph()
        elif caracter == ')':
            subgrafo = grafo
            grafo = pila.pop()
            grafo = nx.compose(grafo, subgrafo)
        elif caracter == '|':
            subgrafo = pila.pop()
            pila.append(grafo.copy())
            grafo = subgrafo
        elif caracter == '*':
            subgrafo = grafo.copy()
            grafo.add_edge(0, 1, label='ε')
            grafo.add_edge(1, 0, label='ε')
            grafo.add_edge(0, 2, label='ε')
            grafo.add_edge(2, 1, label='ε')
            grafo.add_edge(2, 3, label='ε')
            grafo.add_edge(3, 0, label='ε')
            grafo = nx.compose(grafo, subgrafo)
        else:
            grafo.add_edge(0, 1, label=caracter)

    grafo.add_node(2, accepting=True)  # Nodo de aceptación

    return grafo

def main():
    expresion = input("Ingrese una expresión regular (con a-z, A-Z, 0-9, ., |, *, (, ), ε, ∼, Φ): ")

    if validar_expresion_regular(expresion):
        #print("La expresión regular es válida.")
        print(construir_AFND(expresion))
    else:
        print("La expresión regular no es válida.")
main()

