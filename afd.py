from estructura import Th,AFD,Nodo, NodoAFD


class crearAFD:
    afnd = Th()
    afd = AFD()
    nodosArecorrer = []
    nuevosNodos = []


    def __init__(self, afnd):
        self.afnd = afnd
        self.transiciones = []
        self.transicionesParaVisualizar = []
        self.nodosFinales = []

    def AFNDToAFD(self):
        self.armarUniones()
        nodosAFD,transicionesAlfabeto = self.crearTabla()
        #self.verTabla(nodosAFD,transicionesAlfabeto)
        self.construirAFD(nodosAFD,transicionesAlfabeto)
        self.formalizar()
        
        return
    
    def armarUniones(self):
        for nodo in self.afnd.nodos:
            for inicio, etiqueta, destino in self.afnd.transiciones:
                 if((nodo.nombre == inicio) and (destino not in nodo.uniones)):
                    #print("Agregar" , "nombre" , destino, "valor", etiqueta) 
                    nodo.uniones.append({"nombre": destino, "valor" :etiqueta}) 
                    
        
        for nodo in self.afnd.nodos:
            self.buscarTransicionesVacias(nodo)
    
        
    def buscarTransicionesVacias(self,nodo):
            for nodoUnido in nodo.uniones:
                #print("Nodo: ", nodo.nombre, "NodoUnido: ", nodoUnido["nombre"])
                if(nodoUnido["valor"] == "_"):
                    #print("Transicion vacia con ", nodoUnido["nombre"])
                    nodo.transicionesVacias.append(nodoUnido["nombre"])
                    
    def buscarCaracterEnTransicionesVacias(self,uniones,caracter):
        # uniones es un diccionario que contiene todas las uniones de un nodo en este formato{"nombre": destino, "valor" :etiqueta} 
        for union in uniones:
            if(union["valor"] == "_" or union["valor"] == caracter):
                if(union["nombre"] not in self.nodosArecorrer):
                    self.nuevosNodos.append(union["nombre"])
                nuevoNodoARecorrer = self.afnd.retornarNodo(union["nombre"])
                unionesNuevas = nuevoNodoARecorrer.uniones
                if(unionesNuevas != []):
                    #print("Se hace recursion con ", nuevoNodoARecorrer.nombre, " y sus uniones ", unionesNuevas)
                    self.buscarCaracterEnTransicionesVacias(unionesNuevas,caracter)
        return
         
    def crearTabla(self):
        #Lista de caracteres del alfabeto
        alfabeto = self.afnd.alfabeto    
        #Lista de estados del AFD
        nodosAfd = []
        #nodos que en la iteracion son vacios, esta lista es auxiliar para luego ser agregada en las demás
        estados = []
        #Nodo inicial
        inicio =  self.afnd.retornarNodo("q" + str(self.afnd.inicio))
        
        #Corresponde a la lista que contine los nodo que se pueden llegar con transiciones vacia
        # ej: Alfabeto: [a,b] 
        # delta        | a | b |
        # nodos afd    | [[0.estadosAlfabeto] | ,[0.estadosAlfabeto]] |
        # nodos afd    | [[0.estadosAlfabeto],[1.estadosAlfabeto[]] | ,[0.estadosAlfabeto],[1.estadosAlfabeto]] |
        matrizEstadosAlfabeto = []
        
        #Creacion de la lista de caracteres del alfabeto y el tamaño de listas que habrán en estadosAlfabeto
        #La cantidad de listas es igual a la cantidad de caracteres del alfabeto
        for caracter in alfabeto:
            matrizEstadosAlfabeto.append([])
        
        #Define el primer nodo al AFD que corresponde al inicio y sus transiciones vacías
        estados.append(inicio.nombre)
        for nodosTV in inicio.transicionesVacias:
            estados.append(nodosTV)
        nodosAfd.append(estados.copy())
        nodo = self.afnd.retornarNodo("q" + str(self.afnd.inicio))
        self.nodosArecorrer = estados.copy()
        self.buscarCaracterEnTransicionesVacias(nodo.uniones,"_")

    
    
    
    
        """
        alfabeto= [] #Lista de caracteres del alfabeto
        nodosAfd = [] #Nuevos nodos del AFD
        estados = [] #Estado aux
        inicio =  self.afnd.retornarNodo("q" + str(self.afnd.inicio))
        matrizEstadosAlfabeto = [] """ #Matriz de estados del alfabeto
        
        print("------------------------------------------------------------------------------------------------------------")
        estados = []
        #print(matrizEstadosAlfabeto)
        for nodoAfd in nodosAfd:
            #print()
            #print("Nodo AFD ", nodoAfd)
            i = 0
            for caracter in alfabeto:
                #print("Caracter: ", caracter)
                for nombreNodo in nodoAfd:
                    nodo = Nodo()
                    nodo = self.afnd.retornarNodo(nombreNodo)
                    #print("Buscando uniones con el caracter:", caracter , "en el nodo:",nodo.nombre)   
                    self.nodosArecorrer = nodoAfd.copy()
                    self.nuevosNodos = []
                    self.buscarCaracterEnTransicionesVacias(nodo.uniones,caracter)
                    #print("NUEVOS HERMOSOS NODOS: ", self.nuevosNodos)
                    if ((self.nuevosNodos not in estados) and (self.nuevosNodos != [])):estados.append(self.nuevosNodos.copy())   
                #print("Lista auxiliar: ", estados)
                #print("Nodos AFD: ", nodosAfd)
                for nuevosNodosAfnd in estados :
                    if(nuevosNodosAfnd not in nodosAfd):
                        nodosAfd.append(nuevosNodosAfnd)

                #Guardar en formato matriz cada secuencia de nodos
                #print(i)
                if(estados == []):
                    matrizEstadosAlfabeto[i].append("_")
                else:
                    matrizEstadosAlfabeto[i].extend(estados.copy())
                estados.clear()
                i = i + 1
            
        #print("---------------")
        return nodosAfd,matrizEstadosAlfabeto
            
            
    def verTabla(self,nodosAfd,matrizEstadosAlfabeto):
        alfabeto = self.afnd.alfabeto 
        for caracter in alfabeto:
                fila = matrizEstadosAlfabeto[alfabeto.index(caracter)]
                #print("Columna de:", caracter)
                for elemento in fila:
                    print("   ", elemento)

        print("Nodos del afnd ", nodosAfd)  

                                
    def construirAFD(self,nodosAfd,matrizEstadosAlfabeto):
        #print("Comienza la creación del AFD \n")

        afd = self.afd
        alfabeto = self.afnd.alfabeto
        #Crear nodos del AFD
        for nodoAfd in nodosAfd:
            nodo = NodoAFD()

            #nodo.nombre = {"nombre" : "q" + str(nodosAfd.index(nodoAfd)), "grupoNodos" : nodoAfd}
            nodo.nombre = "q" + str(nodosAfd.index(nodoAfd))
            nodo.grupoNodos = nodoAfd
            if("q" + str(self.afnd.final) in nodo.grupoNodos):
                nodo.esFinal = True
            afd.nodos.append(nodo)
            
        for i in range(len(matrizEstadosAlfabeto)):
            filaTransicionI= matrizEstadosAlfabeto[i]
            for j in range(len(filaTransicionI)):
                nodosEnFilaJ = filaTransicionI[j]
                nodoOrigen = afd.nodos[j]
                nodoDestino = afd.devolverNodoPorGrupo(nodosEnFilaJ)
                #Sumidero
                if(nodoDestino == None):
                    nodoDestino = "Sumidero"
                else:
                    nodoDestino = nodoDestino.nombre

                valor = alfabeto[i]
                afd.transiciones.append((nodoOrigen.nombre,valor,nodoDestino))
                
                #print("Nodo origen: ", nodoOrigen.nombre, "Valor: ", valor, "Nodo destino: ", nodoDestino)
                
        #print("Transiciones: ")       
        #print(afd.transiciones)
        self.afn = afd
        self.transiciones = afd.transiciones

    def sumidero(self):
        for caracter in self.afn.alfabeto:
            self.afn.transiciones.append(("Sumidero",caracter,"Sumidero")) 
         
    def formalizar(self):
        #Formalizar de nodos finales
        for nodo in self.afn.nodos:
            if(nodo.esFinal):
                self.nodosFinales.append(nodo.nombre)

        self.afd.alfabeto = self.afnd.alfabeto
        self.afd.nodosIniciales = "q" + str(self.afnd.inicio)
        self.afd.nodosFinales = self.nodosFinales
        nodosNombre = []

        for nodo in self.afd.nodos:
            nodosNombre.append(nodo.nombre)
                    
        print("AFD M= \nK = " , nodosNombre)
        print("\nSigma = " , self.afd.alfabeto)
        print("\nDelta = " , self.afd.transiciones)
        print("\nS = " , self.afd.nodosIniciales)
        print("\nF = " , self.nodosFinales)
    
        