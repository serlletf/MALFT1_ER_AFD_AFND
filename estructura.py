class Nodo:
    def __init__(self ):
        self.transicion = []
        
        
class Th:
    def __init__(self):
        self.inicio = 0
        self.final  = 0
        self.transiciones = []
        
    def agregarTransicion(self,nodo):
        self.transiciones.append(nodo)
        
    def agregarInicioTransicion(self,nodo):
        self.transiciones.insert(0,nodo)
        