import nodos 

nUltimoNodo = 0

def aumenarNUltimoNodo():
    global nUltimoNodo
    nUltimoNodo += 1
    return nUltimoNodo

def thompsonChar(caracter):
    inicio = "q" + str(nUltimoNodo)
    final = "q" + str(aumenarNUltimoNodo())
    return [inicio, caracter, final]
    
def thompsonVacio():
    inicio = "q" + str(nUltimoNodo)
    final = "q" + str(aumenarNUltimoNodo())
    return [inicio, "_", final]

def thompsonConcatenacion(th1, th2):
    q0 = "q" + str(nUltimoNodo)
    q1 = "q" + str(aumenarNUltimoNodo())
    q2 = "q" + str(aumenarNUltimoNodo())
    q3 = "q" + str(aumenarNUltimoNodo())
    
    nodos = [q0, th1, q1],[q1, "_", q2],[q2, th2, q3]
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
    
    nodos = [q0, "_", q1,[q0, "_", q3], [q1, th, q2], [q2, "_", q1], [q2, "_", q3]]
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

th1 = []
operacion = ''

def operar(caracter):
    global th1,operacion
    if (operacion == '.'):
        th1 = thompsonConcatenacion(th1, caracter)
    if (operacion == '|'):
        th1 = thompsonO(th1, caracter)
    if (operacion == '*'):
        th1 = thompsonKleene(th1)  
    if (operacion == '_'):
        th1 = thompsonVacio()
    operacion = ''    
    return


def parsear(expresion):
    global th1,operacion
    print("Asi va ",expresion, "Largo ", len(expresion))
    
    if(len(expresion) == 0):
        return 
    
    parsear(expresion[:-1])
    print("De vuelta para procesar de izquierda a derecha ", expresion)
    
    caracter = expresion[len(expresion) - 1]
    
    #Si hay alguna operacion pendiente, se realiza con el thompson ya existente y el caracter actualmente por procesar
    if(operacion != ''):
        operar(caracter)
        return
        
    #Si se procesa una letra o un numero se hace un thompson de un caracter    
    if(caracter.isalpha() or caracter.isdigit()):
        th1 = thompsonChar(caracter)
        return 
    
    #Como no es un caracter ni un numero, se asume que es una operacion y se agrega como operacion pendiente
    operacion = caracter
    return
     


def toList(expresion):
    lista = []
    for caracter in expresion:
        lista.append(caracter)
    return lista

def main():
    expresion = "a.b|c"
    resultado = parsear(list(expresion))
    print(resultado)
    print(th1)
    
    
main()