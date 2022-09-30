
from flask import Flask, render_template
# Con esta linea creamos la instancia de la clase Flask a nuestro objeto llamado app que será
#la aplicación en si.
app=Flask(__name__)

#Creamos el index de la app, utilizando templates, en html desde la carpteta templates
@app.route("/")
def index():
    #return render_template("index.html", name=900,dato="petrodolar")
    return render_template("calendario.html")
#Las siguientes lineas hacen la ruta principal de la aplicación (/) y a esta pagina le 
# da la funcionalidad de la funcion hola()
@app.route("/mes/")
def hola():
    return("Hola, Mundo")
    #el return devuelve HTML´s enteros

# Las siguientes lineas crean otra página de prueba de calendarioHTML, puedes borrarlo
@app.route("/calen")
def prueba():
    import calendar
    class CustomHTMLCal(calendar.HTMLCalendar):
        cssclasses = [style + " text-nowrap" for style in
                    calendar.HTMLCalendar.cssclasses]
        cssclass_month_head = "text-center month-head"
        cssclass_month = "text-center month"
        cssclass_year = "text-italic lead"
    a=CustomHTMLCal(calendar.HTMLCalendar)
    calendario_HTML = calendar.HTMLCalendar(calendar.MONDAY)
    tablaHTML = calendario_HTML.formatyear(2022, 3)
    print(tablaHTML)
    
    return tablaHTML

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

@app.route("/mes")
def mes(nombre):
    return render_template("mes.html", name=nombre)

#pruebas

@app.route("/calendario")
def calendario():
    return render_template("calendario.html")
    