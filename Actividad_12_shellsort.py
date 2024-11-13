# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:24:09 2024

@author: sebas
"""

def ShellShort (A):
    n=len(A)
    #Empezar con el intervalo igual a la del tam de la lista
    gap = int(n/2) #n//2
    #continuar reduciendo el itervalo hasta llegar a 0
    while gap > 0:
        #recorrer la lista desde el indice igual al 
        #intervalo hasta el final 
        for i in range(gap, n):
            #guardar el valor avtual en una variable 
            #temporal
            temp = A[i]
            #inicializar la variable j en la posicion i
            j = i
            #desplzasar los elementos del subarreglo 
            #ordenado si son mayores que el valor temporal
            while j >= gap and A[j - gap] > temp:
                A[j] = A [j - gap]
                j -= gap
            #insertar el valor temporal en la posicion 
            #cprrecta
            A[j] = temp
        gap//= 2
arreglo = [8,6,7,2,1,4,5,3]
ShellShort(arreglo)
print("Lista Ordenada usando Shell Short: ", arreglo)
                