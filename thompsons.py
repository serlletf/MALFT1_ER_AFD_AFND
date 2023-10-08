import nodos 

nUltimoNodo = 0

def aumenarNUltimoNodo():
    global nUltimoNodo
    nUltimoNodo += 1
    return nUltimoNodo

def thompsonChar(caracter):
    inicio = "q" + str(nUltimoNodo)
    final = "q" + str(aumenarNUltimoNodo())
    return [[inicio, caracter, final]]
    
def thompsonVacio():
    inicio = "q" + str(nUltimoNodo)
    final = "q" + str(aumenarNUltimoNodo())
    return [inicio, "_", final]

def thompsonConcatenacion(th1, th2):
    q0 = "q" + str(nUltimoNodo)
    q1 = "q" + str(aumenarNUltimoNodo())
    q2 = "q" + str(aumenarNUltimoNodo())
    q3 = "q" + str(aumenarNUltimoNodo())
    
    nodos = [[q0, th1, q1],[q1, "_", q2], [q2, th2, q3]]
    return nodos

def thompsonO(th1, th2):
    q0 = "q" + str(nUltimoNodo)
    q1 = th1[0]
    q2 = th1[len(th1)-1]
    q3 = th2[0]
    q4 = th2[len(th2)-1]
    q5 = "q" + str(aumenarNUltimoNodo())
    return [[q0, "_",q1],[q2,"_",q5],[q0, "_",q3],[q4,"_",q5]]

def thompsonKleene(th):
    q0 = "q" + str(nUltimoNodo)
    q1 = "q" + str(aumenarNUltimoNodo())
    q2 = "q" + str(aumenarNUltimoNodo())
    q3 = "q" + str(aumenarNUltimoNodo())
    
    nodos = [[q0, "_", q1],[q0, "_", q3], [q1, th, q2], [q2, "_", q1], [q2, "_", q3]]
    return nodos


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



def obtenerTh2(expresion):
    th2 = []
    for caracter in expresion:
        if(caracter== "("):
            continue
        if (not(caracter.isalpha() or caracter.isdigit())):
            return th2
        th2.append(caracter)
    return th2

def parsear(expresion):
    nNodoActual = 0
    a = lambda i : expresion[i-1]
    b = lambda i : expresion[i+1]
    th1 = []
    th2 = []
    nuevaExpresion = []	
    for i in range(len(expresion)):
        caracter = expresion[i]
        if(caracter== "("):
            nuevaExpresion = capturar_parentesis(expresion)
            if th1== []:
                th1 = nuevaExpresion #Aca se debe hacer una recursion en la nueva expresion
                continue
            th2 = nuevaExpresion
            continue
        if(caracter== ")"):
            continue
        if(caracter=="."):
            th2 = obtenerTh2(expresion[i+1:])
            #th1 = thompsonConcatenacion(th1, th2)
            continue
        if(caracter == "|"):
            #th1 = thompsonO(th1, b(i))
            continue
        if(caracter == "*"):
            #th1 = thompsonKleene(th1)
            continue
        if(caracter == "_"):
            #th1 = thompsonVacio()
            continue
        th1.append(thompsonChar(caracter))
    return th1



def toList(expresion):
    lista = []
    for caracter in expresion:
        lista.append(caracter)
    return lista

def main():
    expresion = "((a.b)|a).c)"
    resultado = parsear(list(expresion))
    print(resultado)
    
    
main()