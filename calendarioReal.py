"""
No funciona bien, solo para calendarioMes


Reazlo de nuevo empezando de 0 tendrias que cojer el mes entero y 
con un split entero e ir dividiendo por grupos, teniendo en cuenta que para la primera fila
tendras 2 elementos, mes y año
para la segunda 7 elementos 
para las demas 7 elementos tambien"""

"""
Para obtener el calendario pero de momento sin turnos
Solo con los dias reales incluidos festivos
De momento por Mes
"""

import calendar as cl
#Para poner el calendario en español utilizamos el utf de español, asi los dias y meses salen en Español
import locale

locale.setlocale(locale.LC_ALL,"es_ES.UTF-8")


year=2022

calendarioMes=cl.month(2022,1)  # el tercer argumento son los espacios, es importante dejarlo sin poner
# pk sino habria que modificar las funciones de extracción de las cabeceras y los dias



def limpiar_year(str_a_split):
    def quitarSaltoLinea(cadena):
        cadenaNueva=""
        for i,j in enumerate(cadena):
            if cadena[i:i+1]=="\n":
                cadenaNueva=cadenaNueva+" "
                continue
            else:
                cadenaNueva=cadenaNueva+j
        return cadenaNueva

    str_a_split=quitarSaltoLinea(str_a_split)
    lista_limpia=str_a_split.split(" ")
    while "" in lista_limpia:
        lista_limpia.remove("")
    #lista_limpia[-1]=lista_limpia[-1][:-1]
    #Quito el año del calendario de la posicion 1
    del(lista_limpia[1])
    return lista_limpia
    print("Esta es la lista de la funcion limpiar:",lista_limpia)


""" Vamos a hacerlo con objetos """    
class Dia:
    num=0
    texto=""
    festivo=False
    turno=""
class Mes:
    dias=[]   
    nombre=""
    num=0    
    dias.append("")

class Calendario:
    year=0
    meses=[]
    meses.append("")


def rellenarMes(calendarioMes):
    mes=Mes()
    mes.nombre=calendarioMes[0].capitalize()
    print(mes.nombre)

    for i in calendarioMes[8:]:
        dia=Dia()
        dia.num=i
        dia.festivo=False
        dia.texto="Sin calcular"
        dia.turno="Sin especificar"
        mes.dias.append(dia)
        
    return mes
    #yearCompleto={mes[0]:{i for i in mes[8:]:"Turno"}}
    """ nombreMes=mes[0]
    dia={}
    lista_dias=[]
    for i in mes[8:]:
        dia={i:["Turno",False]}
        lista_dias.append(dia) """


calendarioReal=Calendario()
calendarioReal.year=2022     #FIXME ESTE VALOR ES TEMPORAL, CAMBIARLO POR EL SUYO (VARIABLE)
for i in range(1,13):
    calendarioMes=cl.month(year,i)
    calendarioMes=limpiar_year(calendarioMes)
    calendarioReal.meses.append(rellenarMes(calendarioMes))

    """ yearCompleto=insertarMes(yearCompleto,calendarioMes)
    print(yearCompleto,len(yearCompleto)) """

print(calendarioReal.meses[1].nombre)

#TODO SEGUIR AQUI...   AÑADIR LOS TURNOS

    