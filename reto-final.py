from abc import ABC, abstractmethod

# Clase abstracta para transporte
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
            print(f"Estudiante {estudiante} asignado a la ruta {self.trayecto}.")
        else:
            print("No hay cupo disponible en esta ruta.")

    def listar_estudiantes(self):
        print(f"Estudiantes en la ruta {self.trayecto}:")
        for est in self.estudiantes:
            print(f"- {est['nombre']} (Asistencia: {'Sí' if est['asistencia'] else 'No'})")

    def marcar_asistencia(self, nombre):
        for est in self.estudiantes:
            if est["nombre"] == nombre:
                est["asistencia"] = True
                print(f"Asistencia marcada para {nombre}.")
                return
        print("Estudiante no encontrado en esta ruta.")

class Microbus(Transporte):
    def tipo(self):
        return "Microbús"

class Camioneta(Transporte):
    def tipo(self):
        return "Camioneta"

class Mototaxi(Transporte):
    def tipo(self):
        return "Mototaxi"

# Registro de rutas y estudiantes
rutas = []

def registrar_ruta():
    trayecto = input("Trayecto: ")
    capacidad = int(input("Capacidad: "))
    conductor = input("Conductor: ")
    print("Tipo de transporte: 1. Microbús 2. Camioneta 3. Mototaxi")
    tipo = input("Seleccione tipo: ")
    if tipo == "1":
        ruta = Microbus(trayecto, capacidad, conductor)
    elif tipo == "2":
        ruta = Camioneta(trayecto, capacidad, conductor)
    elif tipo == "3":
        ruta = Mototaxi(trayecto, capacidad, conductor)
    else:
        print("Tipo no válido.")
        return
    rutas.append(ruta)
    print("Ruta registrada.")

def registrar_estudiante():
    if not rutas:
        print("Primero registre una ruta.")
        return
    nombre = input("Nombre del estudiante: ")
    for idx, ruta in enumerate(rutas):
        print(f"{idx+1}. {ruta.trayecto} ({ruta.tipo()}) - Cupo: {len(ruta.estudiantes)}/{ruta.capacidad}")
    seleccion = int(input("Seleccione la ruta: ")) - 1
    if 0 <= seleccion < len(rutas):
        rutas[seleccion].asignar_estudiante(nombre)
    else:
        print("Ruta no válida.")

def listar_estudiantes_por_ruta():
    for ruta in rutas:
        print(f"\nRuta: {ruta.trayecto} ({ruta.tipo()})")
        ruta.listar_estudiantes()

def marcar_asistencia():
    nombre = input("Nombre del estudiante: ")
    for ruta in rutas:
        ruta.marcar_asistencia(nombre)

def menu():
    while True:
        print("\n1. Registrar ruta")
        print("2. Registrar estudiante")
        print("3. Listar estudiantes por ruta")
        print("4. Marcar asistencia")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_ruta()
        elif opcion == "2":
            registrar_estudiante()
        elif opcion == "3":
            listar_estudiantes_por_ruta()
        elif opcion == "4":
            marcar_asistencia()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()