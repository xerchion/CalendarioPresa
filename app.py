
from flask import Flask, render_template, request, redirect

from datetime import date
import calendarioReal
import Usuarios
import gestionBD
import time

usuario=Usuarios.Usuario()
usuario.nombre="Usuario Anónimo"
mOtro="" #servirá para decir al usuario que está viendo otro turno que no es el suyo
turno=""



year=date.today().year
mensaje=""
colores={"A":"bg-success", "B":"bg-primary", "C":"bg-danger" ,"D":"bg-warning" ,"E":"bg-warning bg-opacity-50" }
coloresdias={"N": "bg-secondary","T":"bg-warning" ,"M":"bg-info" } #Mañana tarde noche



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
            if usuario.turno!="A":
                pass
            anualllamada(usuario)
            renderizar=anualllamada(usuario)
        else:
            usuario.turno=""
            print("El usuario no existe o la contraseña es incorrecta")
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

    return(render_template("calendarioMes.html",mOtro=mOtro,cd=coloresdias,colores=colores,mes=mes,year=year,turno=turno,calendario=calendario))
    #el return devuelve HTML´s enteros
@app.route("/anual",methods=["POST","GET"])
def anual():    
    year=request.form['year']
    turno=request.form['turno']
    if turno=="Elige un Turno":
        turno=usuario.turno
    if turno!=usuario.turno:
        mOtro="Estás viendo otro turno"

    if year=="Elige un año" :
        mOtro=""
        year=date.today().year
    else:
        mOtro=""





    #Colores, dependiendo del turno para los css de bootstrap, usados en cabecera y #TODO menu
    colores={"A":"bg-success", "B":"bg-primary", "C":"bg-danger" ,"D":"bg-warning" ,"E":"bg-warning bg-opacity-50" }
    coloresdias={"N": "bg-secondary","T":"bg-warning" ,"M":"bg-info" } #Mañana tarde noche

    mes=1  # FIXME  ESTO VA A SER PARA PROBAR UN MES EN CONCRETO
    print(year,turno)
    calendario=calendarioReal.calendarioReal(int(year),turno)
    if mOtro:
        print("existe")
        
        time.sleep(5)
    else:
        print("no existe")
    return(render_template("calendarioYear.html",mOtro=mOtro,cd=coloresdias,colores=colores,usuario=usuario.nombre,mes=mes,year=year,turno=turno,calendario=calendario))
# Las siguientes lineas crean otra página de prueba de calendarioHTML, puedes borrarlo
@app.route("/alta",methods=["POST","GET"])
def alta():
    import formularios
    title="Altas"
    mj="cabecera"
    datos=formularios.AltaUsuario(request.form)
    renderizaAlta=render_template("altaUsuario.html",form=datos,msj=mj)
    if request.method=='POST': #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        print("llega por post, de momento sin datos")
        #validamos
        usuario.nombre=datos.nombre.data
        if usuario.nombre!=None:
            print(usuario.nombre)
            usuario.contraseña=datos.contra_usuario.data
            usuario.turno=datos.turno.data
            usuario.correo=datos.correo.data
            usuario.colores=""
            if gestionBD.comprobarUsuario(usuario):
                usuario.nombre="Usuario Anónimo"
                usuario.contraseña=""
                print("el usuario ya esta en la BD aaaaaaaaaaaaaaaaaaa")
                mj="Este usuario ya está registrado !!"
                calendario=calendarioReal.calendarioReal(int(year),usuario.turno)                
                renderizaAlta=render_template("calendarioYear.html",msj=mj,cd=coloresdias,colores=colores,mes=mes,year=year,usuario=usuario.nombre,turno=usuario.turno,calendario=calendario)

            else:
                print("no no no no está y le damos de altaen la BD aaaaaaaaaaaaaaaaaaa")

                mj="el usuario no esta, procedemos a darlo de alta"
                #Guardamos
                if gestionBD.altaUsuario(usuario):
                    #vamos a pagina de confirmación
                    #renderizaAlta=render_template("usuarioExito.html",usuario=usuario.nombre)
                    calendario=calendarioReal.calendarioReal(int(year),usuario.turno)
                    renderizaAlta=render_template("calendarioYear.html",msj=mj,cd=coloresdias,colores=colores,mes=mes,year=year,turno=usuario.turno,usuario=usuario.nombre,calendario=calendario)
        else:            
            
            print(usuario.turno,usuario.nombre,"aquiiiiiiiiiiiiiiiiiiiii")
            calendario=calendarioReal.calendarioReal(int(year),usuario.turno)

            renderizaAlta=render_template("calendarioYear.html",msj=mj,cd=coloresdias,colores=colores,mes=mes,year=year,usuario=usuario.nombre,turno=usuario.turno,calendario=calendario)
            

         
    return renderizaAlta

@app.route("/anualllamada",methods=["POST","GET"])
def anualllamada(usuario):
    mj=""
    turno=usuario.turno
    print ("llega a la llamada del anual")
    #Colores, dependiendo del turno para los css de bootstrap, usados en cabecera y #TODO menu


    mes=1  # FIXME  ESTO VA A SER PARA PROBAR UN MES EN CONCRETO


    calendario=calendarioReal.calendarioReal(int(year),turno)

    return(render_template("calendarioYear.html",msj=mj,cd=coloresdias,colores=colores,mes=mes,year=year,turno=turno,usuario=usuario.nombre,calendario=calendario))
# Las siguientes lineas crean otra página de prueba de calendarioHTML, puedes borrarlo
# con estas lineas activo el debug para no tener que cerrar y abrir el servidor en cada cambio
#que hiciera, de esta manera no hay que hacer ctrl-c para salir del servidor.
# para que funcione no puede ser con "flask run" en la consola, debe ser con "pyton app.py"


#iniciar sesion
@app.route("/iniciarSesion",methods=["POST","GET"])
def iniciarSesion():

    title="Introduccion de datos"
    mensaje="Introuduce los datos"
    print("llega a iniciar sesion")
    
    import formularios
    datos=formularios.Acceso(request.form)
    renderizar= render_template("iniciarSesion.html",title=title,year=year,form=datos,mensaje=mensaje)
    if request.method=='POST' and datos.validate(): #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        print ("Los datos llegan bien: ",datos.contra_usuario.data, "y", datos.nombre.data)
        #validamos
        usuario.nombre=datos.nombre.data
        usuario.contraseña=datos.contra_usuario.data
        renderizar=render_template("iniciarSesion.html",title=title,year=year,form=datos)
        if gestionBD.comprobarUsuario(usuario):
            print("el usuario esta bien y estos son sus datos",usuario.turno)
            if usuario.turno!="A":
                pass
            anualllamada(usuario)
            renderizar=anualllamada(usuario)
        else:
            usuario.turno=""
            print("El usuario no existe o la contraseña es incorrecta")
            mensaje="Este usuario no existe o la contraseña es incorrecta"
            renderizar=render_template("inciarSesion.html",title=title,year=year,form=datos,mensaje=mensaje)
            
    # fin parte nueva formularios


    #return render_template("index.html", name=900,dato="petrodolar")
    return renderizar    



# fin iniciar sesion
if __name__=="__main__":
    app.run(debug=True)





    


