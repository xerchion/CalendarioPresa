
from flask import Flask, render_template, request

from datetime import date
import calendarioReal
import Usuarios
import gestionBD

usuario=Usuarios.Usuario()



year=date.today().year



# Con esta linea creamos la instancia de la clase Flask a nuestro objeto llamado app que será
#la aplicación en si.
app=Flask(__name__)

#Creamos el index de la app, utilizando templates, en html desde la carpteta templates
@app.route("/", methods=["POST","GET"])
    
def index():
    """ parte nueva, de los formularios """
    title="Introduccion de datos"
    mensaje="Introuduce los datos"
    import formularios
    datos=formularios.Acceso(request.form)
    renderizar=render_template("index.html",title=title,year=year,form=datos,mensaje=mensaje)
    if request.method=='POST' and datos.validate(): #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        print ("Los datos llegan bien: ",datos.contra_usuario.data, "y", datos.nombre.data)
        #validamos
        usuario.nombre=datos.nombre.data
        usuario.contraseña=datos.contra_usuario.data
        renderizar=render_template("index.html",title=title,year=year,form=datos)
        if gestionBD.comprobarUsuario(usuario):
            print("el usuario esta bien y estos son sus datos",usuario.turno)
            anualllamada(usuario)
            renderizar=anualllamada(usuario)
        else:
            usuario.turno=""
            mensaje="Este usuario no existe o la contraseña es incorrecta"
            renderizar=render_template("index.html",title=title,year=year,form=datos,mensaje=mensaje)
            
    # fin parte nueva formularios


    #return render_template("index.html", name=900,dato="petrodolar")
    return renderizar

#Las siguientes lineas hacen la ruta principal de la aplicación (/) y a esta pagina le 
# da la funcionalidad de la funcion hola()
@app.route("/mes",methods=["POST","GET"])
def mes():
    year=request.form['year']
    turno=request.form['turno']

    #Colores, dependiendo del turno para los css de bootstrap, usados en cabecera y #TODO menu
    colores={"A":"bg-success", "B":"bg-primary", "C":"bg-danger" ,"D":"bg-warning" ,"E":"bg-warning bg-opacity-50" }
    coloresdias={"N": "bg-secondary","T":"bg-warning" ,"M":"bg-info" } #Mañana tarde noche

    mes=1  # FIXME  ESTO VA A SER PARA PROBAR UN MES EN CONCRETO
    print(year,turno)
    calendario=calendarioReal.calendarioReal(int(year),turno)
    turno=turno.capitalize()
    return(render_template("calendarioMes.html",cd=coloresdias,colores=colores,mes=mes,year=year,turno=turno,calendario=calendario))
    #el return devuelve HTML´s enteros
@app.route("/anual",methods=["POST","GET"])
def anual():
    year=request.form['year']
    turno=request.form['turno']

    #Colores, dependiendo del turno para los css de bootstrap, usados en cabecera y #TODO menu
    colores={"A":"bg-success", "B":"bg-primary", "C":"bg-danger" ,"D":"bg-warning" ,"E":"bg-warning bg-opacity-50" }
    coloresdias={"N": "bg-secondary","T":"bg-warning" ,"M":"bg-info" } #Mañana tarde noche

    mes=1  # FIXME  ESTO VA A SER PARA PROBAR UN MES EN CONCRETO
    print(year,turno)
    calendario=calendarioReal.calendarioReal(int(year),turno)
    turno=turno.capitalize()
    return(render_template("calendarioYear.html",cd=coloresdias,colores=colores,mes=mes,year=year,turno=turno,calendario=calendario))
# Las siguientes lineas crean otra página de prueba de calendarioHTML, puedes borrarlo
@app.route("/alta",methods=["POST","GET"])
def alta():
    import formularios
    title="Altas"
    datos=formularios.AltaUsuario(request.form)

    if request.method=='POST': #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        print("llega por post, de momento sin datos")
        #validamo  
    return render_template("alta.html",form=datos)

@app.route("/anualllamada",methods=["POST","GET"])
def anualllamada(usuario):
    
    turno=usuario.turno
    print ("llega a la llamada del anual")
    #Colores, dependiendo del turno para los css de bootstrap, usados en cabecera y #TODO menu
    colores={"A":"bg-success", "B":"bg-primary", "C":"bg-danger" ,"D":"bg-warning" ,"E":"bg-warning bg-opacity-50" }
    coloresdias={"N": "bg-secondary","T":"bg-warning" ,"M":"bg-info" } #Mañana tarde noche

    mes=1  # FIXME  ESTO VA A SER PARA PROBAR UN MES EN CONCRETO
    print(year,turno)
    calendario=calendarioReal.calendarioReal(int(year),turno)
    turno=turno.capitalize()
    return(render_template("calendarioYear.html",cd=coloresdias,colores=colores,mes=mes,year=year,turno=turno,calendario=calendario))
# Las siguientes lineas crean otra página de prueba de calendarioHTML, puedes borrarlo
# con estas lineas activo el debug para no tener que cerrar y abrir el servidor en cada cambio
#que hiciera, de esta manera no hay que hacer ctrl-c para salir del servidor.
# para que funcione no puede ser con "flask run" en la consola, debe ser con "pyton app.py"
if __name__=="__main__":
    app.run(debug=True)

#  con los siguiente creamos URL's dinámicas
#la ruta recibe un texto y eso lo interpreta como parte de la ruta, dinamicamente, y al ir a esa
#página lo que hace es abrir dicha pagina y utiliza el nombre que le damos en la url para saludar.

""" @app.route("/<string:nombre>/")
def saludo(nombre):
    return f"Hola, {nombre}" """
    # al meter el index.html con templates, las url´s dinamicas me dejan de funcionar

#ahora vamos a crear otra pagina, para poder pasarle una variable al html y saludar



#pruebas


    


