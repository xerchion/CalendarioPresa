
from wtforms import Form
from wtforms import SelectField,StringField,EmailField



class acceso(Form):
    nombre=StringField("Nombre")
    password=StringField("Contraseña")