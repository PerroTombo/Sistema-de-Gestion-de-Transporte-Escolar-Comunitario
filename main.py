from controlador import Controlador
from vista import Vista

if __name__ == "__main__":
    vista = Vista()
    controlador = Controlador(vista)
    controlador.iniciar()