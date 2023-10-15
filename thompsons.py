from estructura import Th,Nodo
from afd import AFD
from visualizar import dibujar


th = Th()
operacion = ""
getNUltimoNodo = lambda th=th: th.final
getNPrimerNodo = lambda th=th: th.inicio

nUltimoNodo = getNUltimoNodo()
nPrimerNodo = getNUltimoNodo()


def aumentarNUltimoNodo():
    global nUltimoNodo
    th.final += 1
    nUltimoNodo = th.final
    return nUltimoNodo

def getNUltimoNodo():
    return nUltimoNodo

def getNPrimerNodo():
    return nPrimerNodo


def armarNodos():
    global th
    nodos = []
    for inicio, etiqueta, destino in th.transiciones:
        if (inicio not in nodos):
            nodos.append(inicio)
            nodo = Nodo()
            nodo.nombre = inicio
            th.nodos.append(nodo)
        if (destino not in nodos):
            nodos.append(destino)
            nodo = Nodo()
            nodo.nombre = destino
            th.nodos.append(nodo)
        
    return

def thompsonChar(caracter):
    global th
    inicio = "q" + str(nUltimoNodo)
    final = "q" + str(aumentarNUltimoNodo())
    th.agregarTransicion((inicio, caracter, final))
    return 
    
def thompsonVacio():
    global th
    inicio = "q" + str(nUltimoNodo)
    final = "q" + str(aumentarNUltimoNodo())
    th.agregarTransicion((inicio, "_", final))

def thompsonConcatenacion(th2):
    global th
    q1 = "q" + str(getNUltimoNodo())
    q2 = "q" + str(aumentarNUltimoNodo())
    q3 = "q" + str(aumentarNUltimoNodo())
    th.agregarTransicion((q1, "_", q2))
    th.agregarTransicion((q2, th2, q3))
    return 

def thompsonO(th2):
    global th
    
    qith1 = "q" + str(th.inicio)
    qfth1 = "q" + str(th.final)
    qith2 = "q" + str(aumentarNUltimoNodo())
    qfth2 = "q" + str(aumentarNUltimoNodo())
    
    nuevoInicio = aumentarNUltimoNodo()
    qi = "q" + str(nuevoInicio)
    qf = "q" + str(aumentarNUltimoNodo())

    th.agregarInicioTransicion((qi,"_",qith1))
    th.agregarInicioTransicion((qi,"_",qith2))
    th.agregarTransicion((qith2,th2,qfth2))
    th.agregarTransicion((qfth2,"_",qf))
    th.agregarTransicion((qfth1,"_",qf))

    th.inicio = nuevoInicio
    
    return 

def thompsonKleene():
    global th
    qith1 = "q" + str(th.inicio)
    qfth1 = "q" + str(th.final)
    qith2 = "q" + str(aumentarNUltimoNodo())
    qfth2 = "q" + str(aumentarNUltimoNodo())
    
    nuevoInicio = aumentarNUltimoNodo()
    qi = "q" + str(nuevoInicio)
    qf = "q" + str(aumentarNUltimoNodo())

    th.agregarInicioTransicion((qi,"_",qith1))
    th.agregarInicioTransicion((qi,"_",qith2))
    th.agregarTransicion((qith2,"_",qfth2))
    th.agregarTransicion((qfth2,"_",qf))
    th.agregarTransicion((qfth1,"_",qf))
    th.agregarTransicion((qfth1,"_",qith1))
    
    return

def capturar_parentesis(expresion):
    grupo = []
    nparentesisAbierto = 0
    for i in range(len(expresion)):
        caracter = expresion[i]
        if(caracter== "("):
            nparentesisAbierto += 1
            if(nparentesisAbierto == 1):continue #Ignorar el primer"(" 
        if(caracter== ")"):
            nparentesisAbierto -= 1
            if(nparentesisAbierto == 0):continue #Ignorar el ultimo"(" 
        if(nparentesisAbierto > 0):
            grupo.append(caracter)
    return grupo


def operar(caracter):
    global th,operacion
    if (operacion == '.'):
        thompsonConcatenacion(caracter)
    if (operacion == '|'):
        thompsonO(caracter)
    """ if (operacion == '*'):
        thompsonKleene() 
    if (operacion == '_'):
       thompsonVacio() """
    operacion = ''    
    return


#Primero debe analizar los parentesis, luego concatenación, despues el | y luego kleene

def parsear(expresion):
    
    global th,operacion
    print("Asi va ",expresion, "Largo ", len(expresion))
    
    if(len(expresion) == 0):
        return 
    
    parsear(expresion[:-1])
    print("De vuelta para procesar de izquierda a derecha ", expresion)
    
    #Va desde derecha a izquierda, para volver y operar recursivamente de izquierda a derecha
    caracter = expresion[len(expresion) - 1]
    
    #Si hay alguna operacion pendiente, se realiza con el thompson ya existente y el caracter actualmente por procesar
    if(operacion != ''):
        operar(caracter)
        return
    if(caracter == '*'):
        thompsonKleene()
        return
    if(caracter == '_'):
        thompsonVacio()
        return
    #Si se procesa una letra o un numero se hace un thompson de un caracter    
    if(caracter.isalpha() or caracter.isdigit()):
        th.inicio = nUltimoNodo
        thompsonChar(caracter)
        return 
    #Como no es un caracter ni un numero, se asume que es una operacion y se agrega como operacion pendiente
    operacion = caracter
    return
     

def determinarAlfabeto(expresion):
    alfabeto = []
    for caracter in expresion:
        if(caracter.isalpha() or caracter.isdigit()):
            if(caracter not in alfabeto):
                alfabeto.append(caracter)
    return alfabeto

def toList(expresion):
    lista = []
    for caracter in expresion:
        lista.append(caracter)
    return lista

def visualizar(afnd):
    vs = dibujar()
    vs.visualizar(afnd)
    
def main():
    global th
    expresion = "a|b"
    parsear(list(expresion))
    th.alfabeto = determinarAlfabeto(expresion)
    afnd = th.transiciones

    print(afnd)
    
    armarNodos()
    visualizar(afnd)
    
    
    afd = AFD(th)
    afd.AFNDToAFD()
    
    
main()