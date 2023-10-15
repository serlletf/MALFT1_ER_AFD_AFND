import networkx as nx
import matplotlib.pyplot as plt

# Datos de las transiciones

class dibujar:
    def mover_maximo_al_final(self, lista):
        if not lista:
            return lista  

        maximo = max(lista)  
        lista.remove(maximo)  
        lista.append(maximo) 
        return lista 
    
    def visualizar(self, transiciones):
        # Crear un gráfico dirigido
        G = nx.DiGraph()
        
        # Agregar nodos y arcos según las transiciones
        for inicio, etiqueta, destino in transiciones:
            G.add_node(inicio)
            G.add_node(destino)
            G.add_edge(inicio, destino, label=etiqueta)

        # Obtener la lista de nodos
        nodos = list(G.nodes())
        # Dibujar el gráfico
        pos = nx.layout.planar_layout(G)
        labels = nx.get_edge_attributes(G, 'label')

        
        node_attributes = {}

        for nodo in nodos:
            if nodo == nodos[0]:  # El primer nodo
                node_attributes[nodo] = 'green'
            elif nodo == nodos[-1]:  # El último nodo
                node_attributes[nodo] = 'red'
            else:
                node_attributes[nodo] = 'skyblue'

        # Dibujar los nodos y arcos con los atributos personalizados
        nx.draw(G, pos, with_labels=True, labels={nodo: nodo for nodo in nodos}, node_color=[node_attributes[nodo] for nodo in nodos], node_size=800)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
        
    
    def visualizarAFD(self, transiciones,nodosFinales):
        # Crear un gráfico dirigido
        G = nx.DiGraph()
        
        # Agregar nodos y arcos según las transiciones
        for inicio, etiqueta, destino in transiciones:
            G.add_node(inicio)
            G.add_node(destino)
            G.add_edge(inicio, destino, label=etiqueta)

        # Obtener la lista de nodos
        nodos = list(G.nodes())
        # Dibujar el gráfico
        pos = nx.layout.planar_layout(G)
        labels = nx.get_edge_attributes(G, 'label')

        
        node_attributes = {}
        nodosFinales
        for nodo in nodos:
            if nodo == nodos[0]:  # El primer nodo
                node_attributes[nodo] = 'green'
            elif nodo == nodos[-1] :  # Nodos finales
                node_attributes[nodo] = 'red'
            else:
                node_attributes[nodo] = 'skyblue'

        # Dibujar los nodos y arcos con los atributos personalizados
        nx.draw(G, pos, with_labels=True, labels={nodo: nodo for nodo in nodos}, node_color=[node_attributes[nodo] for nodo in nodos], node_size=800)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

        



