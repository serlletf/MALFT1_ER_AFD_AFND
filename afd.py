from estructura import Th,Nodo


class AFD:
    afnd = Th()
    nuevosEstados = []

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
                    
    def buscarCaracterEnTransicionesVacias(self,uniones,caracter):
        self.nuevosEstados
        # union es un diccionario en este formato{"nombre": destino, "valor" :etiqueta}
        for union in uniones:
            if(union["valor"] == "_" or union["valor"] == caracter):
                if(union["nombre"] not in self.nuevosEstados):
                    self.nuevosEstados.append(union["nombre"])
                    nodoARecorrer = self.afnd.retornarNodo(union["nombre"])
                    unionesNuevas = nodoARecorrer.uniones
                    if(unionesNuevas != []):
                        print("Se hace recursion con ", nodoARecorrer.nombre, " y sus uniones ", unionesNuevas)
                        self.buscarCaracterEnTransicionesVacias(unionesNuevas,caracter)
        return
         
    def crearTabla(self):
        tabla = []
        nodos = self.afnd.nodos
        alfabeto = self.afnd.alfabeto
        
        #Lista de caracteres del alfabeto
        caracteres = []
        
        #Lista de estados del AFD
        nodosAfd = []
        #nodos que en la iteracion son vacios, esta lista es auxiliar para luego ser agregada en las demás
        estados = []
        #Nodo inicial
        inicio =  self.afnd.retornarNodo("q" + str(self.afnd.inicio))
        final = self.afnd.final
        
        #Corresponde a la lista que contine los nodo que se pueden llegar con transiciones vacia
        # ej: Alfabeto: [a,b] 
        # delta        | a | b |
        # nodos afd    | [[0.estadosAlfabeto] | ,[0.estadosAlfabeto]] |
        # nodos afd    | [[0.estadosAlfabeto],[1.estadosAlfabeto[]] | ,[0.estadosAlfabeto],[1.estadosAlfabeto]] |
        estadosAlfabeto = []
        
        
        #Creacion de la lista de caracteres del alfabeto y el tamaño de listas que habrán en estadosAlfabeto
        #La cantidad de listas es igual a la cantidad de caracteres del alfabeto
        for caracter in alfabeto:
            caracteres.append(caracter)
            estadosAlfabeto.append([])
        
        #Define el primer nodo al AFD que corresponde al inicio y sus transiciones vacías
        estados.append(inicio.nombre)
        for nodosTV in inicio.transicionesVacias:
            estados.append(nodosTV)
        print("EStados ",estados)
        nodosAfd.append(estados.copy())
        print("Nodos AFD ",nodosAfd)
        print("Alfabeto", caracteres)    
        
        print("---------------------")
        estados.clear()
        nodo = self.afnd.retornarNodo("q" + str(self.afnd.inicio))
        
        self.buscarCaracterEnTransicionesVacias(nodo.uniones,"a")
        print("Nuevos estados ",self.nuevosEstados)
    
        """ for caracter in caracteres:
            #print("Caracter: ", caracter)
            for nodoAfd in nodosAfd:
                #print("Nodo AFD ", nodoAfd)
                for nombreNodo in nodoAfd:
                    nodo = Nodo()
                    nodo = self.afnd.retornarNodo(nombreNodo)
                
                    print("Buscando uniones con el caracter: ", caracter , "en el nodo: ",nodo.nombre)
                    for union in nodo.uniones:
                        if(union["valor"] == caracter):
                            estados.append(union["nombre"])
                            print("Se preguntó los estados de ",nodo.nombre, " Se encontro una union con", union["nombre"], " Con el caracter ", caracter)
                            break  """ 
            
        

                                
        
        
        

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
