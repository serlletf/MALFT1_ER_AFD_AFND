import re
import networkx as nx
import matplotlib.pyplot as plt

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


def generarMandala():
    grafo = nx.complete_graph(50)
    grafo = nx.draw_circular(grafo, with_labels=True, node_size=50, node_color='r', font_color='w', font_size=20)
    plt.axis('equal')
    plt.show()
 
def thompsonChar(caracter):
    G = nx.DiGraph()
    inicio = "q0"
    final = "q1"
    nodos = [["q0", caracter, "q1"]]
    # Agregar estados al grafo

    # Agregar transiciones
    G.add_edge(inicio, final, label=caracter)

    # Etiquetar el estado inicial
    G.nodes[inicio]["initial"] = True

    # Etiquetar los estados finales


    # Dibujar el grafo
    pos = nx(G, seed=42)  # Posición de los nodos
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def main():
    #expresion = input("Ingrese una expresión regular (con a-z, A-Z, 0-9, ., |, *, (, ), ε, ∼, Φ): ")
    expresion = "a.b.c"
    if validar_expresion_regular(expresion):
        #print("La expresión regular es válida.")
        #print(construir_AFND(expresion))
        #thompsonChar("a")
        generarMandala()
    else:
        print(f"'{expresion}' no es una expresión regular válida.")

if __name__ == "__main__":
    main()
