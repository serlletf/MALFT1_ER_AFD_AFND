class Nodo:
    def __init__(self ):
        self.nombre= ""
        self.uniones = []
        self.transicionesVacias = []        
        
class Th:
    def __init__(self):
        self.inicio = 0
        self.final  = 0
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
        
    