
from numpy import size
from wtforms import Form
from wtforms import SelectField,StringField,EmailField,IntegerField,PasswordField
from wtforms import validators
from datetime import date

year=int(date.today().year)


class Acceso(Form):
    nombre=StringField("Nombre")
    """
    ,[
        validators.length(min=5,max=10)
    ])"""
    contra_usuario=PasswordField("Contraseña")
    """,[
        validators.length(min=6,max=20)
    ])"""

class AltaUsuario(Form):
    nombre=StringField("Nombre",
    [
        validators.length(min=2,max=20),
        validators.data_required()  
    ])
    contra_usuario=PasswordField("Contraseña",
    [
        validators.length(min=2,max=20),
        validators.data_required()
    ])

# ejemplo
    turno = SelectField(u'Programming Language', choices=[('A', 'Turno A'), ('B', 'Turno B'), \
        ('C', 'Tunro C'),('D', 'Turno D'), ('E', 'Turno E')])
    
    correo=StringField("E-mail",
    [
        validators.length(min=3,max=40),
        validators.data_required()  
    ])
    
class Datos(Form):
    year=IntegerField("Año",
        [
        validators.NumberRange(min=2022,max=2025),
        validators.data_required()
        ])
       
                                                    
    turno=StringField("Turno",
        [
        validators.length(min=2,max=4),
        validators.data_required(message="Campo obligatorio")]
        )
    #ejemplo de Lista desplegable
    #lenguaje = SelectField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])