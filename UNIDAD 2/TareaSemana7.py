# TareaSemana7.py
class ContadorVehiculos:
    # Constructor de la clase
    def __init__(self,autos, acceso):
        # Atributos de la clase
        self.autos = autos
        self.acceso = acceso
    # Método para mostrar el total de vehículos ingresados por un acceso
    def total_vehiculos(self):
        return "{} autos ingresaron por {}".format(self.autos, self.acceso)
    
    # Método destructor de la clase
    def __del__(self):
        print("Se eliminó el contador de vehículos del {}".format(self.acceso))
            
    
vehiculos1 = ContadorVehiculos(150, "Acceso 1")
print(vehiculos1.total_vehiculos())
vehiculos2 = ContadorVehiculos(200, "Acceso 2")
print(vehiculos2.total_vehiculos())
vehiculos3 = ContadorVehiculos(300, "Acceso 3")
print(vehiculos3.total_vehiculos())
del vehiculos1
del vehiculos2
del vehiculos3


class Visitantes:
    # Constructor de la clase
    def __init__(self, vistantes, día):
        # Atributos de la clase
        self.vistantes = vistantes
        self.día = día
    # Método para mostrar el total de visitantes por día
    def total_visitantes(self):
        return "{} visitantes el día {}".format(self.vistantes, self.día)
    
    # Método destructor de la clase
    def __del__(self):
        print("Se eliminó el contador de visitantes del día {}".format(self.día))
    
visitantes_lunes = Visitantes(400, "Lunes")
print(visitantes_lunes.total_visitantes())
visitantes_martes = Visitantes(350, "Martes")   
print(visitantes_martes.total_visitantes())
visitantes_miércoles = Visitantes(300, "Miércoles")
print(visitantes_miércoles.total_visitantes())
del visitantes_lunes
del visitantes_martes  
del visitantes_miércoles


class Asistentes:
    # Constructor de la clase
    def __init__(self, asistentes, evento):
        # Atributos de la clase
        self.asistentes = asistentes
        self.evento = evento
    # Método para mostrar el total de asistentes por evento
    def total_asistentes(self):
        return "{} asistentes al evento {}".format(self.asistentes, self.evento)
    
    # Método destructor de la clase
    def __del__(self):
        print("Se eliminó el contador de asistentes del evento {}".format(self.evento))

Concierto = Asistentes(500, "Concierto de Rock")
print(Concierto.total_asistentes())
Seminario = Asistentes(250, "Seminario de Tecnología")
print(Seminario.total_asistentes())
Aniversario = Asistentes(300, "Aniversario de la Empresa")
print(Aniversario.total_asistentes())
del Concierto
del Seminario
del Aniversario
