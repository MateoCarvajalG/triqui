#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:42:49 2020

@author: mateo
"""

import numpy as np


# matriz=np.zeros((3,3))
# matriz=np.array([[1,0,1],[10,0,0],[10,1,0]])
def imprimeTriqui(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i,j]== 0:
                print('|_', end = '')
            if matriz[i,j]== 1:
                print("|x",end='')
            if matriz[i,j]== 10:
                print("|o",end='')
        print('|')
        
def verifica_juego(matriz):
    sumaFila=np.sum(matriz, axis=0)
    sumaColumna=np.sum(matriz, axis=1)
    sumaDiagonal= np.sum(np.diagonal(matriz))
    matrizT=np.fliplr(matriz)
    sumaDiagonalT=np.sum(np.diagonal(matrizT))
    salida=0
    #gana el jugador 1
    if 3 in sumaFila or 3 in sumaColumna or sumaDiagonal==3 or sumaDiagonalT==3 :
        salida=1
    #gana el jugador 2
        if 30 in sumaFila or 30 in sumaColumna or sumaDiagonal==30 or sumaDiagonalT==30 :
            salida=2
    #termina el juego sin ganador
            if np.sum(matriz) == 54 or np.sum(matriz)==45:
                salida=3
            else:
                #sigue el juego sin ganador y sin llenar el tablero
                salida=4
        
    return salida




       
def jugarTriqui():
    matriz=np.zeros((3,3))
    imprimeTriqui(matriz)
    sigueJuego=True
    jugador1=True
    jugador2=False
    while sigueJuego == True:
        if jugador1 == True:
            print('Turno del jugador #1 (X)')
            cordenada=tuple(input('Ingrese el valor de la casilla que desea jugar, Ej: 1,3 casilla superior izquierda: '))
            x=int(cordenada[0])-1
            y=int(cordenada[2])-1
            if (int(cordenada[0]) < 0 or int(cordenada[0]) > 3)  or (int(cordenada[2]) < 0 or int(cordenada[2]) > 3): 
                print('')
                print('posicion no encontrada, verifique datos de entrada, Ej: 3,1 casilla inferior derecha:')
                continue
            if matriz[x,y] != 0:
                print('')
                print('Casilla no disponible para jugar.')
                continue
            matriz[x , y]= 1
            imprimeTriqui(matriz)
            jugador1=not(jugador1)
        else:
            print('Turno del jugador #2 (O)')
            cordenada=tuple(input('Ingrese el valor de la casilla que desea jugar, Ej: 1,3 casilla superior izquierda: '))
            x=int(cordenada[0])-1
            y=int(cordenada[2])-1
            if (int(cordenada[0]) < 0 or int(cordenada[0]) > 3)  or (int(cordenada[2]) < 0 or int(cordenada[2]) > 3): 
                print('')
                print('posicion no encontrada, verifique datos de entrada, Ej: 3,1 casilla inferior derecha:')
                continue
            if matriz[x,y] != 0:
                print('')
                print('Casilla no disponible para jugar.')
                continue
            matriz[x , y]= 10
            imprimeTriqui(matriz)
            jugador1=not(jugador1)
        estado=verifica_juego(matriz)
        if estado==1:
            print('')
            print('El juego ha terminado, Ganador Jugador #1 ')
            sigueJuego=False
        if estado==2:
            print('')
            print('El juego ha terminado, Ganador Jugador #2 ')
            sigueJuego=False
        if estado==3:
            sigueJuego=False
        if estado==4:
            sigueJuego=True
        
jugarTriqui()