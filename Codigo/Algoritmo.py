#base del algoritmo A* 
#segun vayamos implementando el resto de clases ira que actulizarlo un poco.
import heapq


def A_estrella(inicio, meta):
    #Para la lista abierta se tiene que tener de manera eficiente una estructurad de 
    # datos que mantenga la siguiente esatacion de menor coste arriba osae tiene que ser una lista ordenada por coste.
    #la idea seria usar un Monticulo esta que es una cola de prioridades ya que loslo necesitamos sacar un nodo cada vez
    #por ello que sea una cola de prioridades nos vale y ademas tiene complejidad logaritimica en el add y delete cosa qe nos viene muy bien.

    listaAbierta = []

    #Para la lista cerrado solo queremos saber si de ese nodo ya lo habiamos abierto para esto un hashset nos da complejidad constante por lo que es perfecto

    