import re
import networkx as nx
import matplotlib.pyplot as plt

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
    pos = nx.spring_layout(G, seed=42)  # Posición de los nodos
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
        generarMandala
    else:
        print("La expresión regular no es válida.")
main()

