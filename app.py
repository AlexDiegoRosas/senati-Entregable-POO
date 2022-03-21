from BD.conexion import DAO
import funciones
def menuPrincipal():
    continuar=True
    while(continuar):
        opcionCorrecta=False
        while (not opcionCorrecta):
            print('================ MENÚ PRINCIPAL ==============')
            print('1. -Listar Pacientes')
            print('2. -Registar Paciente')
            print('3. -Actualizar Paciente')
            print('4. -Eliminar Paciente')
            print('5. -Salir')
            print('==============================================')
            opcion = int(input('Seleccione una opcion: '))
            
            if opcion < 1 or opcion > 5:
                print('Opcion incorrecta, ingrese nuevamente...')
            elif opcion == 5:
                continuar = False
                print('!GRACIAS POR USAR ESTE SISTEMA!')
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion(opcion)      
    
def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            pacientes = dao.listarPacientes()
            if len(pacientes) > 0:
                funciones.listarPacientes(pacientes)
            else:
                print("No se encontraron pacientes...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        pacientes = funciones.pedirDatosRegistro()
        try:
            dao.registrarPaciente(pacientes)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            pacientes = dao.listarPacientes()
            if len(pacientes) > 0:
                pacientes = funciones.pedirDatosActualizacion(pacientes)
                if pacientes:
                    dao.actualizarPacientes(pacientes)
                else:
                    print("Datos de paciente a actualizar no encontrados...\n")
            else:
                print("No se encontraron pacientes...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            pacientes = dao.listarPacientes()
            if len(pacientes) > 0:
                DNIEliminar = funciones.pedirDatosEliminacion(pacientes)
                if not(DNIEliminar == ""):
                    dao.eliminarPacientes(DNIEliminar)
                else:
                    print("Datos de paciente a eliminar no encontrados...\n")
            else:
                print("No se encontraron pacientes...")
        except:
            print("Paciente Eliminado")
    else:
        print("Opción no válida...")

menuPrincipal()