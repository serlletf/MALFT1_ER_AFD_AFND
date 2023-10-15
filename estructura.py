nodoCount = 0

#las transiciones de los nodos se guardan en formato de listas
#ej: nodo1.transicion = [["_", nodo2], ["a", nodo3]]
class Nodo:
    def __init__(self):
        global nodoCount
        self.transicion = []
        self.id = nodoCount
        nodoCount += 1

#inicio y final son nodos de clase Nodo, valor por defecto en None
class Th:
    def __init__(self):
        self.inicio = None
        self.final = None
        #self.transiciones = []


    #def agregarTransicion(self, nodo):
    #    self.transiciones.append(nodo)
        
    #def agregarInicioTransicion(self, nodo):
    #    self.transiciones.insert(0, nodo)

    #retorna un nuevo thompson
    def th_o(self, th_sgte):
        nuevoTh = Th()

        #nuevos nodos
        nuevoTh.inicio = Nodo()
        nuevoTh.final = Nodo()

        #transiciones de los nodos

        #transiciones del nuevo inicio
        nuevoTh.inicio.transicion.append(["_", self.inicio])
        nuevoTh.inicio.transicion.append(["_", th_sgte.inicio])

        #transiciones hacia el nuevo final
        self.final.transicion.append(["_", nuevoTh.final])
        th_sgte.final.transicion.append(["_", nuevoTh.final])

        return nuevoTh

    def th_concat(self, th_sgte):
        nuevoTh = Th()
        #concatenacion no crea nodos, solo transiciones

        #nueva transicion epsilon
        self.final.transicion.append(["_", th_sgte.inicio])

        #inicio y final del nuevo thompson
        nuevoTh.inicio = self.inicio
        nuevoTh.final = th_sgte.final

        return nuevoTh

    def th_kleene(self):
        nuevoTh = Th()

        #nuevos nodos
        nuevoTh.inicio = Nodo()
        nuevoTh.final = Nodo()

        #transiciones de los nodos

        #transiciones del nuevo inicio
        nuevoTh.inicio.transicion.append(["_", self.inicio])
        nuevoTh.inicio.transicion.append(["_", nuevoTh.final])

        #transiciones del viejo final
        self.final.transicion.append(["_", self.inicio])
        self.final.transicion.append(["_", nuevoTh.final])

        return nuevoTh
