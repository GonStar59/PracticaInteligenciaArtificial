#base del algoritmo A* 
#segun vayamos implementando el resto de clases ira que actulizarlo un poco.
import heapq


def A_estrella(inicio, meta, grafo):
    #Para la lista abierta se tiene que tener de manera eficiente una estructurad de 
    # datos que mantenga la siguiente esatacion de menor coste arriba osae tiene que ser una lista ordenada por coste.
    #la idea seria usar un Monticulo esta que es una cola de prioridades ya que loslo necesitamos sacar un nodo cada vez
    #por ello que sea una cola de prioridades nos vale y ademas tiene complejidad logaritimica en el add y delete cosa qe nos viene muy bien.

    listaAbierta = []

    #Para la lista cerrado solo queremos saber si de ese nodo ya lo habiamos abierto para esto un hashset nos da complejidad constante por lo que es perfecto

    lisataCerrada = set()

    #Cacularemos la h del nodo inicial y la g que es 0 ya que esatmos en esta y añadimos su sima al coste del nodo inicial
    inicio.setG(0)
    inicio.coste = inicio.getH(meta) + inicio.g

    #Añadimos el nodo inicial a la lista abierta
    heapq.heappush(listaAbierta, inicio)


    #iteramos hatas que hallamos llegado a la meta y como se taratara de un grafo conexo siempre se llega a la meta pero podemos intentar considerar este caso especial de que sea imposible
    #actualmente no considerado
    while meta not in lisataCerrada:
        #sacamos en primero nodo de la lista abierta el nodo en la cima
        actual = heapq.heappop(listaAbierta)

        #obtenemos los vecinos de la estacion actual he iteramos 
        for nuevo in grafo[actual]:
           #si ya esta en la lista cerrada no lo exploramos
            if nuevo in lisataCerrada:
                continue

            #TODO
            #en este caso es un nodo nuevo que habra que añadir a la lista abierta lo añadimos entonces 
            #pueden ocuurrir varias cosas este nodo ya tiene un costecalculado si el nuevo coste es mayor se ignora el nuevo si es menor se actualiza el coste su g y su anterior y hay que eliminar el anterior de la lista abierta y añadir el nuevo
            #Python es una mierda y no tiene su heap la funcion de change key asi que nos buscamos la vida o buscamos otra libreria con un heap de verdad y no la mierda de libreria esatndar de python 


            #este es todo el algoritmo en el fondo asi que fin .


def conseguirG(actual, nuevo):

    #TODO IMPLEMENTAR CUAL VA A SER EL COSTE 
    #la idea seria tener en cuenta los tranbordos y con la informacion que tenemos recolecatada pormos tener en cuenta cuado pas el tren y todo
    #tener en cuenta si esats ya en el tren no tienes que esperara a que pase etc etc etc
    return 0