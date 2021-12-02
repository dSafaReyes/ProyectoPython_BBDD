import mysql.connector

class Conectar_BBDD:
    def __init__(self, nombre_bbdd):
        self.nombre_bbdd = nombre_bbdd
        self.conector = mysql.connector.connect(host="localhost", port="3306", user="root", password="raiz", database=nombre_bbdd, autocommit=True)
        self.cursor_on = self.conector.cursor()
        self.cursor_off = self.conector.cursor().close()


    def crear_tabla(self, nombre_tabla):
        mycursor = self.cursor_on
        mycursor.execute(
            f"CREATE TABLE {nombre_tabla} ("
            f"id int(4) not null auto_increment,"
            f"nombre_puesto varchar(150),"
            f"nombre_empresa varchar(150),"
            f"fecha_empleo date,"
            f"modo_remoto varchar(150),"
            f"tipo_jornada varchar(150),"
            f"tipo_contrato varchar(150),"
            f"salario varchar(150),"
            f"constraint {nombre_tabla}_pk primary key (id)"
            f")"
        )
        return True

    def insertar_datos(self, nombre_tabla, lista_datos):
        mycursor = self.cursor_on
        tabla = (f"INSERT INTO {nombre_tabla} "
                "(nombre_puesto, nombre_empresa, fecha_empleo, modo_remoto, tipo_jornada, tipo_contrato, salario) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        mycursor.execute(tabla, lista_datos)
        return True

    def consulta(self, nombre_tabla):
        mycursor = self.cursor_on
        query = (f"SELECT * FROM {nombre_tabla}")
        return mycursor.execute(query)

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

def eliminar_bbdd(nombre_bbdd):
    mycursor = mysql.connector.connect(host="localhost", port="3306", user="root", password="raiz")
    mycursor.execute(f"DROP DATABASE {nombre_bbdd}")
    mycursor.close()
    return True

if __name__ == '__main__':
    # tecnoempleo = Conectar_BBDD("proyecto_python_tecnoempleo")
    # tecnoempleo.eliminar_bbdd()
    crear_bbdd("proyecto_python_tecnoempleo")
    tecnoempleo = Conectar_BBDD("proyecto_python_tecnoempleo")
    tecnoempleo.crear_tabla("empleo")
    tecnoempleo.insertar_datos("empleo", ["Incident Dispatcher", "SOTEC CONSULTING", "2021-10-21", True, "Jornada Completa", "Contrato No Indefinido", "21.000€-24.000€"])
