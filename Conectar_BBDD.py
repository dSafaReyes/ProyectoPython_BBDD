import mysql.connector

class Conectar_BBDD:
    def __init__(self, nombre_bbdd):
        self.nombre_bbdd = nombre_bbdd
        self.conector = mysql.connector.connect(host="localhost", port="3306", user="root", password="raiz", database=nombre_bbdd)
        self.cursor_on = self.conector.cursor()
        self.cursor_off = self.conector.cursor().close()

    def crear_tabla(self, nombre_tabla):
        mycursor = self.cursor_on
        mycursor.execute(
            f"CREATE TABLE {nombre_tabla} (id int(3), nombre varchar(150), constraint jugador_pk primary key (id)")
        mycursor.close()
        return True

    def insertar_datos(self):
        mycursor = self.cursor_on
        add_employee = ("INSERT INTO employees "
                        "(puesto, empresa, fecha, remoto, jornada, tipo_contrato, salario) "
                        "VALUES (%s, %s, %s, %s, %s)")

        add_salary = ("INSERT INTO salaries "
                      "(puesto, empresa, fecha, remoto, jornada, tipo_contrato, salario) "
                      "VALUES (%(puesto)s, %(empresa)s, %(fech)s, %(remoto)s), %(jornada)s), %(remoto)s), %(tipo_contrato)s), %(salario)s)")

        data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

    def consulta(self):
        mycursor = self.cursor_on
        query = ("SELECT first_name, last_name, hire_date FROM employees "
                 "WHERE hire_date BETWEEN %s AND %s")
        cursor.execute(add_employee, data_employee)

    def eliminar_bbdd(self):
        mycursor = self.cursor_on
        mycursor.execute(f"DROP DATABASE {self.nombre_bbdd}")
        mycursor.close()
        return True

def crear_bbdd(nombre_bbdd):
    conexion = mysql.connector.connect(host="localhost", port="3306", user="root", password="raiz")
    mycursor = conexion.cursor()
    mycursor.execute(f"CREATE DATABASE {nombre_bbdd}")
    return True

if __name__ == '__main__':
    crear_bbdd("proyecto_python_bbdd")
    tecnoempleo = Conectar_BBDD("proyecto_python_bbdd")
    tecnoempleo.eliminar_bbdd()