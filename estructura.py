class Nodo:
    def __init__(self ):
        self.nombre= ""
        #nodo.uniones.append({"nombre": destino, "valor" :etiqueta}) Lista de nombre y valor de uniones de los nodos a los que puede llegar

        self.uniones = []
        #Nombre de los nodos con los que tiene transiciones vacias
        self.transicionesVacias = []        
        
class Th:
    def __init__(self):
        #Alfabeto de la expresion regular en formato lista
        self.alfabeto = []
        self.inicio = 0
        self.final  = 0
        #formato [('q4', '_', 'q2'), ('q4', '_', 'q0')] nodoinicio, simbolo, nodofinal
        self.transiciones = []
        self.nodos = []
    def agregarTransicion(self,nodo):
        self.transiciones.append(nodo)
        
    def agregarInicioTransicion(self,nodo):
        self.transiciones.insert(0,nodo)
        
    def retornarNodo(self, nombre):
        for nodo in self.nodos:
            if(nodo.nombre == nombre):
                return nodo
class AFD:
    def __init__(self):
        self.nodos = []
        self.transiciones = []
        
    def devolverNodoPorGrupo(self, grupo):
        for nodo in self.nodos:
            if(nodo.grupoNodos == grupo):
                return nodo
    def devolverNodoPorNombre(self, nombre):
        for nodo in self.nodos:
            if(nodo.nombre == nombre):
                return nodo

class NodoAFD:
    def __init__(self):
        self.nombre = []
        self.grupoNodos = []
    def retornarNodo(self, nombre):
        for nodo in self.nodos:
            if(nodo.nombre == nombre):
                return nodo
    