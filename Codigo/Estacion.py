class Estacion:
    def __init__(self, nombre, id, latitud, longitud, lineas):
        self.id = id
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.lineas = lineas

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
        return self.coste < other.coste

