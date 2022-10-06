
from numpy import size
from wtforms import Form
from wtforms import SelectField,StringField,EmailField
from wtforms import validators



class Acceso(Form):
    nombre=StringField("Nombre")
    password=StringField("Contraseña")

class Alta_usuario(Form):
    nombre=StringField("Nombre")
    password=StringField("Contraseña")
class Datos(Form):
    year=StringField("Año",[validators.length(min=4,max=4,message='No seas tan listo')])
                                                    # el mensaje no funciona 
    turno=StringField("Turno")