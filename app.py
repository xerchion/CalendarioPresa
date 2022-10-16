
from flask import Flask, render_template, request, redirect, session, url_for,flash

from datetime import date
import calendarioReal
import Usuarios
import gestionBD
import time


usuario=Usuarios.Usuario()
usuario.nombre="Folastero"
mOtro="" #servirá para decir al usuario que está viendo otro turno que no es el suyo
turno=""
hay="HOla"




year=date.today().year
mensaje=""
colores={"A":"bg-success", "B":"bg-primary", "C":"bg-danger" ,"D":"bg-warning" ,"E":"bg-warning bg-opacity-50" }
coloresdias={"N": "bg-secondary","T":"bg-warning" ,"M":"bg-info" } #Mañana tarde noche
nombreUsuarioActivo="Invitado"


# Con esta linea creamos la instancia de la clase Flask a nuestro objeto llamado app que será
#la aplicación en si.
app=Flask(__name__)
app.secret_key = b'eadbfd1f49d6d770ff5cad200d212c74c8f17389df36f7179210af1f9f481741'

#Creamos el index de la app, utilizando templates, en html desde la carpteta templates
@app.route("/", methods=["POST","GET"])
def index():

    turno=usuario.turno
    nombreUsuario=usuario.nombre
    import formularios
    datosCalendario=formularios.Datos(request.form)

    if request.method=='POST': #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        print("Soy index y llega por post")
    else:
        print("llega por otra cosa",year,turno,nombreUsuarioActivo)
        #validamos
        
   
    if 'username' in session:
        nombreUsuario=session["username"]
        turno=usuario.turno
    else:
        nombreUsuario="Invitado"
        usuario.nombre="Invitado"
        turno=usuario.turno
#para la prueba

    session.pop('username', None)

#   activa este return para las pruebas
    #return render_template("pruebas.html",formulario=datosCalendario,year=2022)
# fin de prueba
    return render_template("index.html",formulario=datosCalendario,year=year,turno=turno,colores=colores,mensaje=mensaje,nombre=nombreUsuario)
# ruta de pruebas
@app.route('/pruebas', methods=['GET', 'POST'])
def pruebas():
    flash("federico")
    print("aqui llega a PRUEBAS")
    import formularios
    datosCalendario=formularios.Datos(request.form)
    if request.method=='POST' and datosCalendario.validate(): #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        flash(datosCalendario.nombre.data)
    

    return render_template("pruebas.html",datos=datosCalendario)



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
    if session:
        nombreUsuario=session['username']
        turno=session['turn']
    else:
        nombreUsuario="Invitado"
        turno=""
    year=request.form['year']
    turno=request.form['turno']

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
    return(render_template("calendarioYear.html",mOtro=mOtro,cd=coloresdias,turno=turno,nombre=nombreUsuario,colores=colores,mes=mes,year=year,calendario=calendario))
# Las siguientes lineas crean otra página de prueba de calendarioHTML, puedes borrarlo
@app.route("/alta",methods=["POST","GET"])
def alta():
    import formularios
   
    if session:
        nombreUsuario=session['username']
        turno=session['turn']
    else:
        nombreUsuario="Invitado"

    title="Altas"
    mj="cabecera"
    datos=formularios.AltaUsuario(request.form)
    renderizaAlta=render_template("altaUsuario.html",form=datos,msj=mj,nombre=nombreUsuario)
    if request.method=='POST': #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        print("llega por post, de momento sin datos")
        #validamos
        usuario.nombre=datos.nombre.data
        if usuario.nombre!=None:
            print(usuario.nombre, "lleaga hasa aquilllll")
            usuario.contraseña=datos.contra_usuario.data
            usuario.turno=datos.turno.data
            usuario.correo=datos.correo.data
            usuario.colores=""
            if gestionBD.comprobarUsuario(usuario):
                nombreUsuario="Invitado"
                usuario.contraseña=""
                print("el usuario ya esta en la BD aaaaaaaaaaaaaaaaaaa")
                mj="Este usuario ya está registrado !!"
                calendario=calendarioReal.calendarioReal(int(year),usuario.turno)                
                renderizaAlta=render_template("calendarioYear.html",msj=mj,cd=coloresdias,colores=colores,mes=mes,year=year,nombre=nombreUsuario,turno=usuario.turno,calendario=calendario)

            else:
                print("no no no no está y le damos de altaen la BD aaaaaaaaaaaaaaaaaaa")

                mj="el usuario no esta, procedemos a darlo de alta"
                #Guardamos
                if gestionBD.altaUsuario(usuario):
                    #vamos a pagina de confirmación
                    #renderizaAlta=render_template("usuarioExito.html",usuario=usuario.nombre)
                    calendario=calendarioReal.calendarioReal(int(year),usuario.turno)
                    renderizaAlta=render_template("calendarioYear.html",msj=mj,cd=coloresdias,colores=colores,mes=mes,year=year,turno=usuario.turno,nombre=usuario.nombre,calendario=calendario)
        else:            
            
            print(usuario.turno,usuario.nombre,"aquiiiiiiiiiiiiiiiiiiiii")
            calendario=calendarioReal.calendarioReal(int(year),usuario.turno)

            renderizaAlta=render_template("calendarioYear.html",msj=mj,cd=coloresdias,colores=colores,mes=mes,year=year,nombre=nombreUsuario,turno=usuario.turno,calendario=calendario)
    else:
            nombreUsuario="Invitado"
            print("a la mierda")
            
         
    return renderizaAlta

@app.route("/anualllamada",methods=["POST","GET"])
def anualllamada(usuario):
    print("llega por la llamadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if session:
        nombreUsuario=session['username']
        turno=session['turn']
        #if usuario.turno!=turno:
            #print("puede qqqqqqqqqqqqqqqqqqqqqqqqe lleeeeeeeeeeeeeeeegue")
            #pass # no se muy bien que hacer aqui, seria para que no cambie el color
    else:
        nombreUsuario="Invitado"
        turno=""
    mj=""
    turno=usuario.turno
    turnoCabecera=usuario.turno #esta podria usarse para diferenciar la cabecera del turno del calendario
    
 
    mes=1  # FIXME  ESTO VA A SER PARA PROBAR UN MES EN CONCRETO


    calendario=calendarioReal.calendarioReal(int(year),turno)

    return(render_template("calendarioYear.html",msj=mj,cd=coloresdias,colores=colores,mes=mes,year=year,turno=turno,nombre=nombreUsuario,calendario=calendario))
# Las siguientes lineas crean otra página de prueba de calendarioHTML, puedes borrarlo
# con estas lineas activo el debug para no tener que cerrar y abrir el servidor en cada cambio
#que hiciera, de esta manera no hay que hacer ctrl-c para salir del servidor.
# para que funcione no puede ser con "flask run" en la consola, debe ser con "pyton app.py"


#iniciar sesion

@app.route('/login', methods=['GET', 'POST'])
def login():
  
    import formularios
    datos=formularios.Acceso(request.form)
    if request.method=='POST' and datos.validate(): #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        usuario.nombre=datos.nombre.data
        usuario.contraseña=datos.contra_usuario.data
        if gestionBD.comprobarUsuario(usuario):
            session['username'] = usuario.nombre
            session['turn']=usuario.turno
            session['active']=True
                        #mensaje de introducido bien
            anualllamada(usuario)        
            return anualllamada(usuario)
    #else:
        #logout()
    return render_template("iniciarSesion.html",form=datos,nombre=nombreUsuarioActivo,colores=colores)
        





@app.route('/logout')
def logout():
    # remove the username from the session if it's there


    session.pop('username', None)
    session.pop('active',None)
    #print(session['turn'])
    #del session['username']
    usuario.nombre="Invitado"
    usuario.turno="federico"
    return redirect(url_for('index'))

# fin iniciar sesion
if __name__=="__main__":
    app.run(debug=True)





    


