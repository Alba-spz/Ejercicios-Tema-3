class Nave:
    def __init__(self, nombre, longitud, tripulacion, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros

    def __str__(self):
        return (f"Nave: {self.nombre}, Longitud: {self.longitud}m, "
                f"Tripulación: {self.tripulacion}, Pasajeros: {self.pasajeros}")

    def capacidad_total(self):
        return self.tripulacion + self.pasajeros