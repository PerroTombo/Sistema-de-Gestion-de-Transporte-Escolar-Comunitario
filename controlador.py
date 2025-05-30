from modelo import Microbus, Camioneta, Mototaxi

class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.rutas = []

    def iniciar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "1":
                self.registrar_ruta()
            elif opcion == "2":
                self.registrar_estudiante()
            elif opcion == "3":
                self.listar_estudiantes_por_ruta()
            elif opcion == "4":
                self.marcar_asistencia()
            elif opcion == "5":
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida.")

    def registrar_ruta(self):
        trayecto, capacidad, conductor, tipo = self.vista.solicitar_datos_ruta()
        if tipo == "1":
            ruta = Microbus(trayecto, capacidad, conductor)
        elif tipo == "2":
            ruta = Camioneta(trayecto, capacidad, conductor)
        elif tipo == "3":
            ruta = Mototaxi(trayecto, capacidad, conductor)
        else:
            self.vista.mostrar_mensaje("Tipo no válido.")
            return
        self.rutas.append(ruta)
        self.vista.mostrar_mensaje("Ruta registrada.")

    def registrar_estudiante(self):
        if not self.rutas:
            self.vista.mostrar_mensaje("Primero registre una ruta.")
            return
        nombre = self.vista.solicitar_nombre_estudiante()
        seleccion = self.vista.mostrar_rutas(self.rutas)
        if 0 <= seleccion < len(self.rutas):
            mensaje = self.rutas[seleccion].asignar_estudiante(nombre)
            self.vista.mostrar_mensaje(mensaje)
        else:
            self.vista.mostrar_mensaje("Ruta no válida.")

    def listar_estudiantes_por_ruta(self):
        for ruta in self.rutas:
            self.vista.mostrar_estudiantes_ruta(ruta)

    def marcar_asistencia(self):
        nombre = self.vista.solicitar_nombre_estudiante()
        for ruta in self.rutas:
            mensaje = ruta.marcar_asistencia(nombre)
            if "marcada" in mensaje or "no encontrado" not in mensaje:
                self.vista.mostrar_mensaje(mensaje)
                return
        self.vista.mostrar_mensaje("Estudiante no encontrado en ninguna ruta.")
