from estructura import Th
from visualizar import dibujar


th = Th()
operacion = ''
getNUltimoNodo = lambda th=th: th.final

nUltimoNodo = getNUltimoNodo()

def aumentarNUltimoNodo():
    global nUltimoNodo
    th.final += 1
    nUltimoNodo = th.final
    return nUltimoNodo

def getNUltimoNodo():
    return nUltimoNodo

def thompsonChar(caracter):
    global th
    inicio = "q" + str(nUltimoNodo)
    final = "q" + str(aumentarNUltimoNodo())
    th.agregarTransicion((inicio, caracter, final))
    return 
    
def thompsonVacio():
    inicio = "q" + str(nUltimoNodo)
    final = "q" + str(aumentarNUltimoNodo())
    return [inicio, "_", final]

def thompsonConcatenacion(th2):
    global th
    q1 = "q" + str(getNUltimoNodo())
    q2 = "q" + str(aumentarNUltimoNodo())
    q3 = "q" + str(aumentarNUltimoNodo())
    th.agregarTransicion((q1, "_", q2))
    th.agregarTransicion((q2, th2, q3))
    return 

def thompsonO(th1, th2):
    q0 = "q" + str(nUltimoNodo)
    q1 = th1[0]
    q2 = th1[len(th1)-1]
    q3 = th2[0]
    q4 = th2[len(th2)-1]
    q5 = "q" + str(aumentarNUltimoNodo())
    return [[q0, "_",q1],[q2,"_",q5],[q0, "_",q3],[q4,"_",q5]]

def thompsonKleene(th):
    q0 = "q" + str(nUltimoNodo)
    q1 = "q" + str(aumentarNUltimoNodo())
    q2 = "q" + str(aumentarNUltimoNodo())
    q3 = "q" + str(aumentarNUltimoNodo())
    
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




def operar(caracter):
    global th,operacion
    if (operacion == '.'):
        thompsonConcatenacion(caracter)
    if (operacion == '|'):
        th = thompsonO(th, caracter)
    if (operacion == '*'):
        th = thompsonKleene(th)  
    if (operacion == '_'):
        th = thompsonVacio()
    operacion = ''    
    return


def parsear(expresion):
    global th,operacion
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
        th.inicio = nUltimoNodo
        thompsonChar(caracter)
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
    global th
    expresion = "a.b.c"
    parsear(list(expresion))
    
    afnd = th.transiciones
    print(afnd)
    
    
    
    
    
main()