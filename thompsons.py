import nodos 

def thompsonChar(caracter):
    inicio = "q0"
    final = "q1"
    return [inicio, caracter, final]
    
def thompsonVacio():
    inicio = "q0"
    final = "q2"
    return [inicio, "_", final]

def thompsonConcatenacion(th1, th2):
    nodos = [["q0", th1, "q1"],["q1", "_", "q2"], ["q2", th2, "q2"]]
    return nodos

def thompsonO(th1, th2):
    inicio = th1[0]
    final = th2[th2.size() - 1]
    return [inicio, "_", th2]

def thompsonKleene(th):
    inicio = "q0"
    final = "q2"
    nodos = [["q0", "_", "q1"],["q0", "_", "q3"], ["q1", th, "q2"], ["q2", "_", "q1"], ["q2", "_", "q3"]]
    return nodos


nodos = []
def capturar_parentesis(expresion):
    grupo = []
    for i in range(len(expresion) - 1 ):
        caracter = expresion[i]
        if(caracter== "("):
            grupo.append(i)
        elif(caracter== ")"):
            grupo.append(i)
    return grupo


def parsear(expresion):
    a = lambda i : expresion[i-1]
    b = lambda i : expresion[i+1]
    th1 = []
    th2 = []
    nuevaExpresion = []	
    
    for i in range(len(expresion) - 1 ):
        caracter = expresion[i]
        
        if(caracter== "("):
            nuevaExpresion = capturar_parentesis(expresion)
            print(nuevaExpresion)
            continue
        if(caracter== ")"):
            continue
        if(caracter == "."):
            th1 = thompsonConcatenacion(a(i), b(i))
            print(th1)
            continue
        if(caracter == "|"):
            th1 = thompsonO(th1, b(i))
            print(th1)
            continue
        if(caracter == "*"):
            th1 = thompsonKleene(th1)
            print(th1)
            continue
        if(caracter == "_"):
            th1 = thompsonVacio()
            print(th1)
        th1 =  caracter
        return th1


def toList(expresion):
    lista = []
    for caracter in expresion:
        lista.append(caracter)
    return lista

def main():
    expresion = "a.b.c"
    parsear(list(expresion))
    
    
main()