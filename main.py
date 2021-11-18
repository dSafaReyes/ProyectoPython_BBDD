import mysql.connector

def crear_bbdd():
    conexion = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="raiz"
    )
    mycursor = conexion.cursor()
    mycursor.execute("CREATE DATABASE proyectopython_bbdd")
    mycursor.close()
    return True

def eliminar_bbdd():
    conexion = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="raiz"
    )
    mycursor = conexion.cursor()
    mycursor.execute("DROP DATABASE proyectopython_bbdd")
    mycursor.close()
    return True

if __name__ == '__main__':
    print(eliminar_bbdd())
