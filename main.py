import mysql.connector

def conectar_bbdd():
    conexion = mysql.connector.connect(host="localhost", port="3306", user="root", password="raiz")
    cursor = conexion.cursor()
    return cursor

def crear_bbdd(nombre_bbdd):
    conexion = conectar_bbdd()
    mycursor = conexion.cursor()
    mycursor.execute(f"CREATE DATABASE {nombre_bbdd}")
    mycursor.close()
    return True

def usar_bbdd(nombre_bbdd):
    mycursor = conectar_bbdd()
    mycursor.execute(f"USE {nombre_bbdd}")
    return True

def crear_tabla(nombre_tabla, nombre_bbdd):
    mycursor = conectar_bbdd()
    usar_bbdd(nombre_bbdd)
    mycursor.execute(f"CREATE TABLE {nombre_tabla} (id int(3), nombre varchar(150), constraint jugador_pk primary key (id)")
    mycursor.close()
    return True

def eliminar_bbdd(nombre_bbdd):
    mycursor = conectar_bbdd()
    mycursor.execute(f"DROP DATABASE {nombre_bbdd}")
    mycursor.close()
    return True


if __name__ == '__main__':
    print(eliminar_bbdd("proyecto_python_bbdd"))
    #print(crear_bbdd("proyecto_python_bbdd"))
    #print(crear_tabla("jugador", "proyecto_python_bbdd"))
