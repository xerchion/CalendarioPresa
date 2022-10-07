import sqlite3

#TODO pasar los usuarios
import Usuarios
usuPrueba=Usuarios.Usuario()
usuPrueba.id=60
usuPrueba.nombre="Jose"
usuPrueba.contraseña="Abcdff"
usuPrueba.turno="C"

#Creo la conexion a la tabla
conexion=sqlite3.connect('cal_press.db')

#Creo el cursor, que sirve para hacer consultas o mandatos SQL
cursor=conexion.cursor()

#Hago una creación de tabla #TODO ESTO HABRA QUE QUITARLO SINO DA ERROR PK YA ESTA CREADA LA TABLA
cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios (
    id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    contraseña TEXT NOT NULL,
    turno TEXT NOT NULL,
    cejemplo TEXT) """)
#HASTA AQUI HABRA QUE BORRAR PARA PODER SEGUIR.....
#TODO Alta usuario
    #Introduccion estática, este ya esta en la BBDD
#cursor.execute("INSERT INTO usuarios VALUES ('11','Pedro','vertigo','c')")

#Ahora una introducción dinámica usando variables, en este caso un objeto de la calse Usuarios
# lo que le pasamos como parametros de los datos debe ser una TUPLA..
datos_alta=(usuPrueba.id,usuPrueba.nombre,usuPrueba.contraseña,usuPrueba.turno)

# PARA DAR DE ALTA HAY 3 FORMAS DE HACERLO

#  FORMA 1
# Esta es una manera de hacerlo, la comento pk no puede meter los mismos datos que la siguiente
#ya que el ID seria el mismo...

#cursor.execute("INSERT INTO usuarios VALUES (?,?,?,?)", datos_alta)

#  FORMA 2
# otra forma de hacer esto sería asi: (en el video dicen que se pasa un diccionario, 
# pero a mi me funciona bien con tupla como en el de arriba)

#cursor.execute("INSERT INTO usuarios VALUES (:id,:nombre,:contraseña,:turno)", datos_alta)

#  FORMA 3
# En esta, seria la opcion de no pasarle todos los campos, y esto se haria asi:
# para ello me he inventado el campo cejemplo y no le he puesto la propiedad NOT NULL

#cursor.execute("INSERT INTO usuarios (id,nombre,contraseña,turno )VALUES (:id,:nombre,:contraseña,:turno)", datos_alta)

#importante no olvidar guardar los datos tras un alta o modificación
conexion.commit()

# hacer consulta de un todo
cursor.execute("SELECT * FROM usuarios")
usuario=cursor.fetchall()
print("todos los usuarios: ",usuario)
print(" ")


#TODO hacer busquedas de cosas
#empecemos con el ID
cursor.execute("SELECT * FROM usuarios WHERE id=?",("24",))
usuario=cursor.fetchall()
print("Usuario especifico, con id 24",usuario)

#buscquemos por contraseña
cursor.execute("SELECT * FROM usuarios WHERE contraseña=?",("Abcdff",))
usuario=cursor.fetchall()
#si no existe me devuelve una lista vacia, hagamos la comprobación antes de del print
if usuario:
    print("Usuario especifico, con contraseña Abcdff",usuario)  

# cerrar siempre la conesxion a la bd al terminar.
conexion.close()