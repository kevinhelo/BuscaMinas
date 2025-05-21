'''
Kevin Herrera Lopez
Requerimiento no Funcionales

Buscaminas

0. 10x10
1. Guarde Y Recupere
2.Informar Cuantas Jugadas lleva el jugador, y cuantas minas les falta por adivinar

Requerimiento Funcional 

0. 20 Minas (Aleatoriamente)
1. La primera Jugada es libre (No Muere)
3. Si descubre Mina, Pierde
4. Si no Descubre Mina sigue jugando / Decir cuantas minas hay alrededor 
5. Informar Si Gana



X = Mina
1= SEGURO
0 = BLANCO

'''

import random 

def tablero():
    filas = 10
    columnas = 10
    matriz = [[0]*columnas for c in range(filas)]
    GuardarMapa = open ("Tablero10x10.txt","w")
    mapa = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            mapa += str(matriz[i][j])
    GuardarMapa.write(mapa)
    GuardarMapa.close
    
def JugadasUNO():


    LeerTablero = open ("Tablero10x10.txt","r")
    matrizMapa = LeerTablero.readlines()

    GuardarMapa = open("Tablero10x10.txt","w")
    
    #LEER MAPA
    nue = ""
    for i in range(len(matrizMapa)):
        for j in range(len(matrizMapa[i])):
            nue += matrizMapa[i][j]
    matriz = []
    for c in range(10):
        fila = []
        for z in range(10):
            fila.append(nue[c*10 + z])
        matriz.append(fila)
    
    #IMPRIME MAPA DEL JUGADOR
    for ii in range(len(matriz)):
        print(matriz[i])
    
    #POSICION DEL PRIMER MOVIMIENTO

    print("DIGITE DONDE DESEA HACER SU PRIMER MOVIMIENTO: ")
    x1 = int(input("COORDENADA X: "))
    y1 = int(input("COORDENADA Y: "))
    matriz[x1][y1] = "1"

    for map in range(len(matriz)):
        print(matriz[map])
    
    #GUARDAR MAPA
    act = ""
    for ii in range(len(matriz)):
        for jj in range(len(matriz[i])):
            act += matriz[ii][jj]
    GuardarMapa.write(act)
    GuardarMapa.close()
    

def MinasAleatorias():

    LeerTablero = open ("Tablero10x10.txt","r")
    matrizMapa = LeerTablero.readlines()
    #print(matrizMapa)

    #HACERLO CADENA
    nue = ""
    for i in range(len(matrizMapa)):
        for j in range (len(matrizMapa[i])):
            nue += matrizMapa[i][j]
    #print(nue)

    matriz = []
    for c in range(10):
        fila = []
        for z in range(10):
            fila.append(nue[c*10 + z])
        matriz.append(fila)

    for cc in range(len(matriz)):
        print(matriz[cc])

    ci = 0
    minas = 20


def Jugar():
    tablero()
    JugadasUNO()
    

#MinasAleatorias()

def eje ():
    filas = 10
    colum = 10
    total = ""

    coorx = random.randint(0,colum - 1)
    coory = random.randint(0,filas - 1)

    total = str(coorx) +" "+ str(coory)
    print(total)


eje() 
    
