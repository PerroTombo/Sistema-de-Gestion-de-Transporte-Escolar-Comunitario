from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, trayecto, capacidad, conductor):
        self.trayecto = trayecto
        self.capacidad = capacidad
        self.conductor = conductor
        self.estudiantes = []

    @abstractmethod
    def tipo(self):
        pass

    def asignar_estudiante(self, estudiante):
        if len(self.estudiantes) < self.capacidad:
            self.estudiantes.append({"nombre": estudiante, "asistencia": False})
            return f"Estudiante {estudiante} asignado a la ruta {self.trayecto}."
        else:
            return "No hay cupo disponible en esta ruta."

    def listar_estudiantes(self):
        return self.estudiantes

    def marcar_asistencia(self, nombre):
        for est in self.estudiantes:
            if est["nombre"] == nombre:
                est["asistencia"] = True
                return f"Asistencia marcada para {nombre}."
        return "Estudiante no encontrado en esta ruta."

class Microbus(Transporte):
    def tipo(self):
        return "Microbús"

class Camioneta(Transporte):
    def tipo(self):
        return "Camioneta"

class Mototaxi(Transporte):
    def tipo(self):
        return "Mototaxi"
