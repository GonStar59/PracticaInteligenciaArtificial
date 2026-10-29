from Constates import VELOCIDAD_MAXIMA

class Estacion:
    def __init__(self, nombre, id, latitud, longitud, lineas):
        self.id = id
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.lineas = lineas
        self.coste = float('inf')  # Inicializamos el coste como infinito
        self.anterior = None  # Inicializamos la estación anterior como None


    def __str__(self):
        return f"Estación: {self.nombre}, Ubicación: ({self.latitud}, {self.longitud}), Líneas: {', '.join(self.lineas)}"

    #el coste sera el coste estimado que se tiene hasta el final 
    def nuevoCoste(self, coste):
        self.coste = coste

    #el anteriror sera la esatcion anterior de la que se viene.
    def setAnterior(self, anterior):
        self.anterior = anterior

    #Definimos comparacion de esatciones dependiendo de su coste muy simple pero es necesario para las librerias como heap
    def __lt__(self, other):
        if self.coste == other.coste: #para que no haya empates es por asegurar cada uo tien id distintos asi que perfecto
            return self.id < other.id


        return self.coste < other.coste

    def setG(self, g):
        self.g = g


    def getH(self, meta):

        #Calculamos la distancia entre la estacion actual y la estacion final 
        distacia = ((self.latitud - meta.latitud) ** 2 + (self.longitud - meta.longitud) ** 2) ** 0.5

        #como nustra estimacion queremos q se base en el tiempo que se tarda y h tiene que ser siempre menor que el g real dividimos por la velocidad maxima
        return distacia / VELOCIDAD_MAXIMA