def listarPacientes(pacientes):
    print("\nPacientes: \n")
    contador = 1
    for cur in pacientes:
        datos = "{0}. DNI: {1} | Nombre: {2} | Sexo: {3} | Correo: {4} | Fecha De Nacimiento: {5} | Telefono: {6}"
        print(datos.format(contador, cur[0], cur[1], cur[2],cur [3],cur [4], cur[5]))
        contador = contador + 1
    print(" ")
    
def pedirDatosRegistro():
    dniCorrecto = False
    while(not dniCorrecto):
        dni = input("Ingrese su DNI: ")
        if len(dni) == 8:
            dniCorrecto = True
        else:
            print("DNI incorrecto: Debe tener 8 dígitos.")

    nombre = input("Ingrese nombre: ")
    
    sexoCorrecto = False
    while (not sexoCorrecto):
        sexo = input("Ingrese su sexo: ")
        if sexo == 'Masculino' or 'Femenino':
            sexoCorrecto=True
        else:
            print('Ingrese nuevamente su sexo [Masculino o Femenino]')
    
    correoCorecto = False
    while(not correoCorecto):
        correo = input ('Ingrese su correo: ')
        correoCorecto= True
    nacimiento = input('Ingrese su fecha de Nacimiento: ')
    
    telefono = input('Ingrese su número de telefono: ')
    pacientes = (dni, nombre, sexo, correo, nacimiento, telefono)
    return pacientes

def pedirDatosActualizacion(pacientes):
    listarPacientes(pacientes)
    existeDNI = False
    DNIEditar = int(input("Ingrese el número de DNI del paciente a editar: "))
    for dato in pacientes:
        if dato[0] == DNIEditar:
            existeDNI = True
            break

    if existeDNI:
        nombre = input("Ingrese nombre a modificar:  ")
        sexo = input("Ingrese su sexo: ")  
        correo = input ('Ingrese su correo: ')
        nacimiento = input('Ingrese su fecha de Nacimiento: ')
        telefono = input('Ingrese su número de telefono: ')

        pacientes = (DNIEditar, nombre, sexo, correo, nacimiento, telefono)
    else:
        pacientes = None

    return pacientes


def pedirDatosEliminacion(pacientes):
    listarPacientes(pacientes)
    existeDNI = False
    DNIEditar = int(input("Ingrese el número de DNI del paciente a eliminar: "))
    for dato in pacientes:
        if dato[0] == DNIEditar:
            existeDNI = True
            break
        
    if not existeDNI:
        DNIEliminar = ""

    return DNIEliminar