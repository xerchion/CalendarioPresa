import sqlite3



#Creo la conexion a la tabla
conexion=sqlite3.connect('usuarios.db')

#Creo el cursor, que sirve para hacer consultas o mandatos SQL
cursor=conexion.cursor()

#Hago una creación de tabla #TODO ESTO HABRA QUE QUITARLO SINO DA ERROR PK YA ESTA CREADA LA TABLA
cursor.execute(""" CREATE TABLE usuarios (
    nombre TEXT,
    contraseña TEXT,
    turno TEXT) """)
#HASTA AQUI HABRA QUE BORRAR PARA PODER SEGUIR.....