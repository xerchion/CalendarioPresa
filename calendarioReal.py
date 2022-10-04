

import calendar as cl
#Para poner el calendario en español utilizamos el utf de español, asi los dias y meses salen en Español
import locale

locale.setlocale(locale.LC_ALL,"es_ES.UTF-8")


year=2023      # FIXME  ESTE AÑO ES EL QUE SE DEBE PASAR COMO PARAMETRO A ELECCION DEL USUSARIO
turno="c"       # FIXME  ESTE AÑO ES EL QUE SE DEBE PASAR COMO PARAMETRO A ELECCION DEL USUSARIO

calendarioMes=cl.month(year,1)  # el tercer argumento son los espacios, es importante dejarlo sin poner
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


# Objetos para el calendario 
class Dia:
    num=0   # ES REDUNDANTE, EL INDICE DE meses.dia nos da esto tambien
    texto=""    # Supuestamente dia de la semana, SIN USAR (4-10)
    festivo=False
    turno=""
class Mes:
    dias=[]   
    nombre=""
    num=0    # ES REDUNDANTE, EL INDICE DE meses nos da esto tambien SIN USAR
    dias.append(Dia)    # añado un dia en blanco para que el indice 0 quede vacío
class Calendario:
    year=0
    meses=[]
    meses.append(Mes)   # añado un dia en blanco para que el indice 0 quede vacío
    

def rellenarMes(calendarioMes):
    """
    funcion que coge un mes y nos rellena el nombre y los dias segun el mes que le pasamos
    como mes real obtenido previamente, nos devuelve un mes con sus dias reales y los valores 
    inicializados por defecto
    """
    mes=Mes()
    mes.dias=[]
    mes.nombre=calendarioMes[0].capitalize()
    """ print(calendarioMes) """
    for i in calendarioMes[8:]:
        dia=Dia()
        dia.num=i
        dia.festivo=False
        dia.texto="Sin calcular"
        dia.turno="Sin especificar"
        mes.dias.append(dia)
    return mes



calendarioReal=Calendario()
calendarioReal.year=year     #FIXME ESTE VALOR ES TEMPORAL, CAMBIARLO POR EL SUYO (VARIABLE)
for i in range(1,13):
    calendarioMes=cl.month(year,i)
    calendarioMes=limpiar_year(calendarioMes)
    calendarioReal.meses.append(rellenarMes(calendarioMes))

    """ yearCompleto=insertarMes(yearCompleto,calendarioMes)
    print(yearCompleto,len(yearCompleto)) """


from generarPatron import generarPatron
patron=generarPatron(year,turno)



""" print(patron)
print("Longitud:  ",len(patron))    """ 

#// TODO   AÑADIR LOS TURNOS

iPatron=0 # recorreremos la lista patron con un indice
# los for para rellenar los turnos en el calendario
for mes in calendarioReal.meses[1:]:
    for dia in mes.dias[1:]:
        dia.turno=patron[iPatron]
        iPatron+=1

#// TODO  LOS FESTIVOS

import holidays
for i in holidays.Spain(years=year).items():
    mesFestivo=i[0].month
    diaFestivo=i[0].day
    calendarioReal.meses[mesFestivo].dias[diaFestivo].festivo=True

# El calendario completo en --->   calendarioReal






