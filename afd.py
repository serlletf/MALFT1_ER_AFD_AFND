from estructura import Th,Nodo


class AFD:
    afnd = Th()
    
    def __init__(self, afnd):
        self.afnd = afnd

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
            
        
    

                

        