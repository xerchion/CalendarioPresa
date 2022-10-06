from tkinter.tix import Select
from wtforms import Form
from wtforms import SelectField,StringField


class Datos(Form):
    year=StringField("Año")
    turno=StringField("Turno")
