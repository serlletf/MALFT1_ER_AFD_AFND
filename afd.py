from estructura import Th,Nodo


class AFD:
    afnd = Th()
    
    def __init__(self, afnd):
        self.afnd = afnd

    def AFNDToAFD(self):
        self.armarUniones()
        self.crearTabla()
        return
    
    def armarUniones(self):
        uniones = [] 
        for nodo in self.afnd.nodos:
            for inicio, etiqueta, destino in self.afnd.transiciones:
                 if((nodo.nombre == inicio) and (destino not in nodo.uniones)):
                    #print("Agregar" , "nombre" , destino, "valor", etiqueta) 
                    nodo.uniones.append({"nombre": destino, "valor" :etiqueta}) 
                    
        
        for nodo in self.afnd.nodos:
            self.buscarTransicionesVacias(nodo)
            print("Transiciones vacias del nodo ", nodo.nombre, " : ",  nodo.transicionesVacias)
    
        
    def buscarTransicionesVacias(self,nodo):
            for nodoUnido in nodo.uniones:
                #print("Nodo: ", nodo.nombre, "NodoUnido: ", nodoUnido["nombre"])
                if(nodoUnido["valor"] == "_"):
                    #print("Transicion vacia con ", nodoUnido["nombre"])
                    nodo.transicionesVacias.append(nodoUnido["nombre"])
                    #self.buscarTransicionesVacias(self.afnd.retornarNodo(nodoUnido["nombre"]))
          
    def crearTabla(self):
        tabla = []
        nodos = self.afnd.nodos
        alfabeto = self.afnd.alfabeto
        caracteres = []

        nodosAfd = []
        estados = []
        inicio =  self.afnd.retornarNodo("q" + str(self.afnd.inicio))
        final = self.afnd.final
        estadosAlfabeto = []
        for caracter in alfabeto:
            caracteres.append(caracter)
            estadosAlfabeto.append([])
        
        estados.append(inicio.nombre)
        for nodosTV in inicio.transicionesVacias:
            estados.append(nodosTV)
        nodosAfd.append(estados)    
          
        print(caracteres)                  
        print(estados)
        print(nodosAfd)
        
        
        

def convertir_afnd_a_afd(tabla_transiciones_afnd, estados_iniciales_afnd):
    estados_afd = set()
    estados_afd.add(estados_iniciales_afnd)
    alfabeto_afd = set()
    transiciones_afd = {}

    # Construir el conjunto de estados iniciales del AFD
    # Puedes tener múltiples estados iniciales en el AFND, así que comienza con el conjunto de estados iniciales

    # Construir el alfabeto del AFD
    for estado, transiciones in tabla_transiciones_afnd.items():
        alfabeto_afd.update(transiciones.keys())

    # Inicializar una cola para procesar conjuntos de estados
    cola = [estados_iniciales_afnd]

    # Procesar los conjuntos de estados
    while cola:
        conjunto_actual = cola.pop(0)
        estados_afd.add(conjunto_actual)
        transiciones_afd[conjunto_actual] = {}

        for simbolo in alfabeto_afd:
            destino = set()
            for estado in conjunto_actual:
                if simbolo in tabla_transiciones_afnd[estado]:
                    destino.update(tabla_transiciones_afnd[estado][simbolo])
            if destino:
                transiciones_afd[conjunto_actual][simbolo] = destino
                if destino not in estados_afd:
                    cola.append(destino)

    return estados_afd, alfabeto_afd, transiciones_afd
