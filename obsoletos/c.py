"""
No funciona bien, solo para septiembre


Reazlo de nuevo empezando de 0 tendrias que cojer el mes entero y 
con un split entero e ir dividiendo por grupos, teniendo en cuenta que para la primera fila
tendras 2 elementos, mes y año
para la segunda 7 elementos 
para las demas 7 elementos tambien"""



import calendar as cl
#Para poner el calendario en español utilizamos el utf de español, asi los dias y meses salen en Español
import locale
from tkinter.tix import INTEGER
locale.setlocale(locale.LC_ALL,"es_ES.UTF-8")

#serie de turnos
lista_repeticion=[2,2,3,4,3,2,2,5,2,3,2,5]
fecha_inicio="fecha inicial aqui"

septiembre=cl.month(2022,1)  # el tercer argumento son los espacios, es importante dejarlo sin poner
# pk sino habria que modificar las funciones de extracción de las cabeceras y los dias

print(septiembre)

#vamos a destriparlo
print(len(septiembre))
parte=septiembre[150:155] #25
for i,j in enumerate(septiembre):
    print(i,j)

def limpiar_str(str_a_split):
    lista_limpia=str_a_split.split(" ")
    while "" in lista_limpia:
        lista_limpia.remove("")
    lista_limpia[-1]=lista_limpia[-1][:-1]
    return lista_limpia
    print("Esta es la lista de la funcion limpiar:",lista_limpia)

def extraer_cabecera_mes(calendario_mes):
    # Funcion que devuelve el mes y el año de la cabecera del calendario de un mes
    # devuelve en este orden el Nombre del Mes Con la primera en mayusculas
    # y el año con cuatro digitos y entero
    cabecera=calendario_mes[0:25]   #del mes esta es la cabecera
    cabecera=limpiar_str(cabecera)
    mes=cabecera[0].capitalize()  
    year=int(cabecera[1][:4])
    return mes,year
def extraer_cabecera_dias(calendario_mes):
    # posiciones 18 a 38
    cabecera_dias=calendario_mes[18:39]
    cabecera_dias=limpiar_str(cabecera_dias)
    
    return cabecera_dias
def extraer_semana_x(calendario_mes,semana_x:INTEGER):
    #extraigo los dias de la semana que se le pase por argumento semana_x al calendario pasado
    # semanas del 1 a 5, controlar que tenga esas semanas, puede ser de 4 semanas...
    semana=[]
    #semana 1   posiciones 39 a 59
    #semana 2   posiciones 61 a 81
    #semana 3   posiciones 81 a 102
    #semana 3   posiciones 102 a 123
    posiciones=0
    if semana_x==1:
        posiciones=(39,60)
    elif semana_x==2:
        posiciones=(61,81)
    elif semana_x==3:
        posiciones=(81,102)
    elif semana_x==4:
        posiciones=(102,123)
    elif semana_x==5:
        posiciones=(123,138)
    semana=calendario_mes[posiciones[0]:posiciones[1]]
    semana=limpiar_str(semana)
    print(semana)

    # para mantener los huecos a principio de mes
    huecos=0
    semana_entera=[]
    print(semana[0])
    huecos=7-len(semana)
          
    for i in range(huecos):
        semana_entera.append(" ")
    if semana[0]=="1":
        semana_entera=semana_entera+semana
    else:
        semana_entera=semana+semana_entera
    print("Semana entera, con huecos",semana_entera)
   
    return semana_entera

# ahora necesito crear un objeto con todos los datos
mes_completo={"mes":extraer_cabecera_mes(septiembre)[0],"cabecera_dias":extraer_cabecera_dias(septiembre)}

print(extraer_cabecera_mes(septiembre))
mes,año=extraer_cabecera_mes(septiembre)
print(año)
for i in range(1,6,1):
    print("Semana :",i)
    extraer_semana_x(septiembre,i)
    mes_completo[i]=extraer_semana_x(septiembre,i)
extraer_cabecera_dias(septiembre)


print("Aqui esta el conjunto de datos completo: ",mes_completo)
#veamos los festivos
""" import holidays
for i in holidays.Spain(years=2023).items():
    print(i) """






