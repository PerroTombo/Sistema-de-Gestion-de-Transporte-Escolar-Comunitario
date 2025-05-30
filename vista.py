class Vista:
    def mostrar_menu(self):
        print("\n1. Registrar ruta")
        print("2. Registrar estudiante")
        print("3. Listar estudiantes por ruta")
        print("4. Marcar asistencia")
        print("5. Salir")
        return input("Seleccione una opción: ")

    def solicitar_datos_ruta(self):
        trayecto = input("Trayecto: ")
        capacidad = int(input("Capacidad: "))
        conductor = input("Conductor: ")
        print("Tipo de transporte: 1. Microbús 2. Camioneta 3. Mototaxi")
        tipo = input("Seleccione tipo: ")
        return trayecto, capacidad, conductor, tipo

    def solicitar_nombre_estudiante(self):
        return input("Nombre del estudiante: ")

    def mostrar_rutas(self, rutas):
        for idx, ruta in enumerate(rutas):
            print(f"{idx+1}. {ruta.trayecto} ({ruta.tipo()}) - Cupo: {len(ruta.estudiantes)}/{ruta.capacidad}")
        return int(input("Seleccione la ruta: ")) - 1

    def mostrar_estudiantes_ruta(self, ruta):
        print(f"\nRuta: {ruta.trayecto} ({ruta.tipo()})")
        for est in ruta.listar_estudiantes():
            print(f"- {est['nombre']} (Asistencia: {'Sí' if est['asistencia'] else 'No'})")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
