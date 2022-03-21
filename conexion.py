import mysql.connector
from mysql.connector import Error


class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='crudclinica'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarPacientes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM pacientes ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                print ('conexion exitosa')
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarPaciente(self, position):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO pacientes (dni_pacientes, nombre, sexo, correo, fecha_nacimiento, telefono) VALUES ('{0}', '{1}', '{2}','{3}','{4}','{5}')"
                cursor.execute(sql.format(position[0], position[1], position[2], position[3], position[4], position[5]))
                self.conexion.commit()
                print("¡Paciente registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarPacientes(self, dato):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE pacientes SET nombre = '{0}', sexo = '{1}', correo = '{2}', fecha_nacimiento = '{3}', telefono ='{4}' WHERE dni_pacientes = '{5}'"
                cursor.execute(sql.format(dato[1], dato[2], dato[3], dato[4], dato[5], dato[0]))
                self.conexion.commit()
                print("¡Paciente actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarPacientes(self, DNIPacienteEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM pacientes WHERE dni_pacientes = '{0}'"
                cursor.execute(sql.format(DNIPacienteEliminar))
                self.conexion.commit()
                print("¡Paciente eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))