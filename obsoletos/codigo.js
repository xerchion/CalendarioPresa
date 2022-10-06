
// Tareas a Ralizar






// 			Pedir valores por pantalla, bien por listas o introduciendolos, mejor por listas
						// Turno y año.





// Declaración inicial de variables
let añoUsuario;	//Valores por defecto
let turnoUsuario="C"; //Valores por defecto

// Al año le vamos a dar el año acutal
let fechaAhora= new Date();
añoUsuario=fechaAhora.getFullYear();


const nombresDias= ["Lunes","Martes","Miercoles","Jueves", "Viernes", "Sabado","Domingo"];
const nombresMeses=["E n e r o","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
let diasFijosMes=[31,28,31,30,31,30,31,31,30,31,30,31];
let totalDiasAño=365; // esta variable es para el paso de los turnos a los dias
	// cambiará a 366 si el año es bisiesto, lo hace en la funcion comprobar bisiesto.

let valorTurnoInicio2022;  



// funciones generales
 //----------------------------------------------------------------

function generar()   // Crear año, calendario, patron y mostrar calendario

{
	// Creamos el año  pasandole el año del usuario
	año=new Año(añoUsuario);

// rellenamos el año con los dias y meses (ya controlamos bisiesto y todo)
	año.rellenaAño(añoUsuario);

// Creamos el calendario con todo lo demas relleno
	calendario=new Calendario(año,turnoUsuario);

	calendario.rellenarCalendarioTurno(turnoUsuario);


	patron=new ValoresTurnos;

	patron.generarValores();

	// Mostramos el calendario
	calendario.mostrarAño();
}

function bisiesto(year)		// Funion para comprobar si el año es bisiesto
		{ 										// si lo es, cambia los dias de febrero a 29
			if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) 
			{
				return true;
			}
			else return false;
		}



class ValoresTurnos   // para el patron de turnos
{
	constructor(){}

generarValores=(turno)=>
{
	
	
	// vector con las repeticiones por valor
	let repValor=[2,2,3,4,3,2,2,5,2,3,2,5];
	// vector con los turnos como valores
	let valor=["M","T","N","D","M","T","N","D","M","T","N","D"]

	let patron=new Array();

	let dias=0;

	while (dias<400000)
	{
		for (let iValor=0;iValor<valor.length;iValor++)
		{	
			
			for (let jRepValor=1;jRepValor<=repValor[iValor];jRepValor++)
			{
				//patron[dias]=`"${valor[iValor]}"`
				patron[dias]=valor[iValor];
				//document.write("    Repetición  "+jRepValor);
				dias++;

			}
			
		}
	}
	return patron; // Devuelve un array con el patrón de los turnos diarios de 40000 posiciones.
}
}	


class Dia
{
	constructor (nombreDia,numeroDia,numeroDiaTotal,turnoToca) 
	{
		this.nombreDia=nombreDia;
		this.numeroDia=numeroDia;
		
		this.numeroDiaTotal=numeroDiaTotal;
		this.turnoToca=turnoToca;
	} 

}

class Mes
{
	constructor (nombreMes,numeroMes,diasTotales,dias) 
	{
		this.nombreMes=nombreMes;
		this.numMes=numeroMes;
		this.diasTotales=diasTotales;
		this.dias=dias;						// este es un array de objetos de la clase DIA, todos los del mes
		// this.festivos=festivos;				// este es un array numeros de dias festivos  NO USADO BORRAR
	}
	
}

class Año
{
	constructor (numeroAño,meses)
	{
		this.numeroAño=numeroAño;
		this.meses=meses;
	}
	rellenaAño=(numeroAño)=>		// Esta funcion crea y genera los meses y dias 
								// de todo el años, le faltan los festivos y los turnos. ??
	{
		
		
		// llamamos a la funcion de comprobacion de bisiesto para preparar febrero
		if (bisiesto(this.numeroAño)){
				diasFijosMes[1]=29;
				totalDiasAño=366;
			}
			;
		
		// Rellenamos los meses-------------------------------------------------

			
		let mesArray=new Array(11); // iniciamos el array temporal de meses
		let kDiaTotal=1; 			// variable que controla el numero de dia total 
							//en el año (ejem. 2 de febrero dia 32)
		
		for (let i=0;i<12;i++)
		{
			
			let diasArray=new Array(diasFijosMes[i]);  // iniciamos el array temporal de dias(segun el mes)
			// Rellenamos ahora los dias de ese mes
			
			for (let j=0;j<diasFijosMes[i];j++)
			{
				// probando a calcular el dia de la semana
				let fechaTemp= new Date(this.numeroAño,i,j);
				let diaSemana=nombresDias[fechaTemp.getDay()];
				diasArray[j]=new Dia(diaSemana,j+1,kDiaTotal++,"Sin meter")
				//	constructor (nombreDia,numeroDia,numeroDiaTotal,turnoToca) 
			}
			mesArray[i]=new Mes(nombresMeses[i],i+1,diasFijosMes[i],diasArray,0);
			//constructor (nombreMes,numeroMes,diasTotales,dias,festivos)
		}


				
 		this.meses=mesArray;// le pasamos los arrays al objeto
	}

}

class Calendario
{
	constructor (añoInt, turno)
	{
		this.año=añoInt;
		this.turno=turno;
	}

mesIndividualNuevo=(mesTemp)=>{

		let numeroMesTEMP=mesTemp;
 		let mes = Array();
 		mes=this.año.meses[numeroMesTEMP];
 		 
 		let turno=this.turno;

 		

		let turnoLargo;		// el texto para la clase segun el turno


		// Creamos los primeros grid-container, en este laso los de la cabecera del mes

		nuevoElemento=document.createElement("DIV");
		let gridContainer=contenedor.appendChild(nuevoElemento);
		gridContainer.classList.add("grid-container");
		// div del nombre del mes
		nuevoElemento=document.createElement("DIV");
		let gridCabeceraMes=gridContainer.appendChild(nuevoElemento);
		gridCabeceraMes.classList.add("grid-item");
		gridCabeceraMes.textContent=mes.nombreMes;

		//ahora creamos los items de la cabecera semanal
				// Lunes
		nuevoElemento=document.createElement("DIV");
		let gridCabeceraSemLu=gridContainer.appendChild(nuevoElemento);
		gridCabeceraSemLu.classList.add("grid-item");
		gridCabeceraSemLu.textContent="Lu";
				// Martes
		nuevoElemento=document.createElement("DIV");
		let gridCabeceraSemMa=gridContainer.appendChild(nuevoElemento);
		gridCabeceraSemMa.classList.add("grid-item");
		gridCabeceraSemMa.textContent="Ma";
				// Miercoles
		nuevoElemento=document.createElement("DIV");
		let gridCabeceraSemMi=gridContainer.appendChild(nuevoElemento);
		gridCabeceraSemMi.classList.add("grid-item");
		gridCabeceraSemMi.textContent="Mi";
				// Jueves
		nuevoElemento=document.createElement("DIV");
		let gridCabeceraSemJu=gridContainer.appendChild(nuevoElemento);
		gridCabeceraSemJu.classList.add("grid-item");
		gridCabeceraSemJu.textContent="Ju";

				// Viernes
		nuevoElemento=document.createElement("DIV");
		let gridCabeceraSemVi=gridContainer.appendChild(nuevoElemento);
		gridCabeceraSemVi.classList.add("grid-item");
		gridCabeceraSemVi.textContent="Vi";
				// Sabado
		nuevoElemento=document.createElement("DIV");
		let gridCabeceraSemSa=gridContainer.appendChild(nuevoElemento);
		gridCabeceraSemSa.classList.add("grid-item");
		gridCabeceraSemSa.textContent="Sa";
				// Domingo
		nuevoElemento=document.createElement("DIV");
		let gridCabeceraSemDo=gridContainer.appendChild(nuevoElemento);
		gridCabeceraSemDo.classList.add("grid-item");
		gridCabeceraSemDo.textContent="Do";		
		// esto se podria mejorar haciendo un bucle que coja las 2 primeras letras de
		// un array con los dias y despues una funcion que haga los 4 pasos.

// Divs en blanco para los primeros dias segun el dia de la semana del primer dia del mes

		let diaSemanaInicioMes= nombresDias.indexOf(mes.dias[0].nombreDia);
		for (let j=1;j<=diaSemanaInicioMes;j++)
		{
			nuevoElemento=document.createElement("DIV");
			let gridEnBlanco=gridContainer.appendChild(nuevoElemento);
			gridEnBlanco.classList.add("grid-item");
			gridEnBlanco.textContent="";
			gridEnBlanco.id=("hueco");

	
		}// fin for j creacion huecos al inicio del mes


 		

 		// repetimos para cada día
 		for (let i=0;i<diasFijosMes[numeroMesTEMP];i++)
 		{
 			turno=mes.dias[i].turnoToca;
 			
		// seleccionamos el texto largo segun el turno
 			switch (turno){
				case "M":
					turnoLargo="Mañana";
					break;
				case "T":
					turnoLargo="Tarde";
					break;
				case "N":
					turnoLargo="Noche";
					break;
				case "D":
					turnoLargo="Descanso";
					break;
				case "F":
					turnoLargo="Festivo";
					break;

				} // fiin del switch
 				

 				turnoLargo=turnoLargo.toLowerCase();

 				nuevoElemento=document.createElement("DIV");
				let gridDiaItem=gridContainer.appendChild(nuevoElemento);
				gridDiaItem.classList.add("grid-item");
				gridDiaItem.textContent=i+1;
				gridDiaItem.id=turnoLargo;	

			}// fin del for  de dias

 				
				// vieeeeejoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

	
 		

 	
 	}// fin funcion mes individual


// Se trata de una funcion que rellene el calendario segun el patron del turno elegido 
 	rellenarCalendarioTurno=(turno)=>
 	{
	
// revisa compentarios desde aqui, seguramente sobrarán cosas-------------------
//-----------------------------------------------------------------------------


		

			// segun el turno asignamos los valores de inicio para 1-1-2022
		switch (turno)
		{
			case "A":
				valorTurnoInicio2022=19+diasInicioCalendario;
				break;
			case "B":
				valorTurnoInicio2022=33+diasInicioCalendario;
				break;		
			case "C":
				valorTurnoInicio2022=12+diasInicioCalendario;
				break;
			case "D":
				valorTurnoInicio2022=26+diasInicioCalendario;
				break;
			case "E":
				valorTurnoInicio2022=5+diasInicioCalendario;
				break;


		}
		let iTurnos=valorTurnoInicio2022;  // esta  es para controlar los dias que vamos rellenado

		let patronGeneral=new ValoresTurnos;

		let patron=new Array();
		patron=patronGeneral.generarValores();



		while (iTurnos<totalDiasAño+diasInicioCalendario)  // sumo el total de dias para que coja ese tramo del patron
			 for (let iMeses=0;iMeses<12;iMeses++)
			 {
				for (let iDias=0;iDias<diasFijosMes[iMeses];iDias++)
				{
					this.año.meses[iMeses].dias[iDias].turnoToca=patron[iTurnos];
					iTurnos++;
				}	
					
		 	 }// fin for iMeses
		 	 
		 //rellenar los festivos
		 this.año.meses[0].dias[0].turnoToca="F";  // 1 de enero, añonuevo
		 this.año.meses[0].dias[5].turnoToca="F";  // 6 de enero Reyes
		 this.año.meses[1].dias[27].turnoToca="F";  // 28 de febrero, dia de Andalucia
		 this.año.meses[3].dias[24].turnoToca="F";	// 25 de abril, fiesta local pero no se de k
		 this.año.meses[4].dias[0].turnoToca="F";  // 1 de mayo, dia del trabajador
		 this.año.meses[7].dias[14].turnoToca="F";  // 15 de agosto, Día de la virgen
		 this.año.meses[7].dias[28].turnoToca="F";	// 29 de agosto, fiesta local pero no se de k

		 this.año.meses[9].dias[11].turnoToca="F";  // 12 de Octubre, Día del Pilar
		 this.año.meses[10].dias[0].turnoToca="F";  // 1 de Noviembre, Todos los Santos
		 this.año.meses[11].dias[6].turnoToca="F";  // 6 de Diciembre, Dia de la constitución
		 this.año.meses[11].dias[8].turnoToca="F";  // 8 de Diciembre, Dia de la Inmaculada.



 	}// fin funcion rellenarCalendarioTurno

 	

//  	

 	mostrarAño = () =>
 	{
 		
 		for (let i=0;i<12;i++){
 			this.mesIndividualNuevo(i);
 		}
 	
 	
 	}// fin MostraAñoPRUEBA


}// fin clase


// La parte principal del programa empieza AQUI
// declaraciones previas;
let nuevoElemento,cabecera, contenedor, turnoElement, añoElement, listaTurnos,escuchaListaTurnoUsuario;

function crearCabecera(){
		nuevoElemento=document.createElement("DIV");
		cabecera=document.body.appendChild(nuevoElemento);
		cabecera.classList.add("cabecera");

		// Creamos el DIV contenedor, donde iran los grid
		nuevoElemento=document.createElement("DIV");
		contenedor=document.body.appendChild(nuevoElemento);
		contenedor.classList.add("contenedor");

		// Elementos de la cabecera:   turno y año
						//Turno
		nuevoElemento=document.createElement("DIV");
		turnoElement=cabecera.appendChild(nuevoElemento);
		turnoElement.classList.add("turno");
		turnoElement.textContent="Turno "+turnoUsuario;
						//año
		nuevoElemento=document.createElement("DIV");
		añoElement=cabecera.appendChild(nuevoElemento);
		añoElement.classList.add("año");
		añoElement.textContent=añoUsuario;

}	


crearCabecera();
// NUEVO
// AÑADIR LA ESCUCHA DEL TITULO (TURNO)

function borrarElements(){
	cabecera.remove();
	contenedor.remove();
}
								// MODIFICAR ESTO PARA QUE LO HAGA CON UN MENÚ


function clickBotonAño(){


// aqui vamos a hacer el campo de introduccion de datos


// fin de lo nuevo 31-3

do { 
		añoUsuario=prompt("Introduce el año del que deseas el calendario:   (Mayor de 2022)");
	} while (añoUsuario<2022)   // Bucle para que validación de año 
		// Bucle para que solo deje meter Los turnos correctos.
	
borrarElements();
crearCabecera();

// calculamos los dia para el inicio del calendario
diasInicioCalendario=0;  // variable general, hay que subirla al principio
for (i=2022;i<añoUsuario;i++){
	
		if (bisiesto(i)) 
			{
				diasInicioCalendario=diasInicioCalendario+366;
			}
			else{	diasInicioCalendario=diasInicioCalendario+365; }
	
	
	} // fin del for de calculo de dias 

generar();
 }   // fin  acciones del boton del Año


 function clickBotonTurno(){

		// do { 
		// 	turnoUsuario=prompt("De que turno quieres el calendario:  A  B  C  D  E");
		// 	turnoUsuario=turnoUsuario.toUpperCase();
		// } while (turnoUsuario!="A" && turnoUsuario!="B" && turnoUsuario!="C" && turnoUsuario!="D" && turnoUsuario!="E")  
		// listaTurnoUsuario.style.visibility="visible";
		borrarElements();
		// Creamos el select
		listaTurnos=document.createElement("SELECT");
		
		listaTurnos.classList.add("listaTurnoUsuario");
		listaTurnos.setAttribute("onchange","cambiarValorTurno()");
		document.body.appendChild(listaTurnos);
		//Creamos cada una de las opciones
		// default para decirle que elija
		
		let turnoDef=document.createElement("OPTION");
		turnoDef.setAttribute("value","");
		// turnoDef.setAttribute("default");
		listaTurnos.appendChild(turnoDef);
		let textoTurnoDef=document.createTextNode("Elige un Turno");
		turnoDef.appendChild(textoTurnoDef);		
		// Turno A
		let turnoA=document.createElement("OPTION");
		turnoA.setAttribute("value","A");
		listaTurnos.appendChild(turnoA);
		let textoTurnoA=document.createTextNode("Turno A");
		turnoA.appendChild(textoTurnoA);
		// Turno B
		let turnoB=document.createElement("OPTION");
		turnoB.setAttribute("value","B");
		listaTurnos.appendChild(turnoB);
		let textoTurnoB=document.createTextNode("Turno B");
		turnoB.appendChild(textoTurnoB);
		// Turno C
		let turnoC=document.createElement("OPTION");
		turnoC.setAttribute("value","C");
		listaTurnos.appendChild(turnoC);
		let textoTurnoC=document.createTextNode("Turno C");
		turnoC.appendChild(textoTurnoC);
		// Turno D
		let turnoD=document.createElement("OPTION");
		turnoD.setAttribute("value","D");
		listaTurnos.appendChild(turnoD);
		let textoTurnoD=document.createTextNode("Turno D");
		turnoD.appendChild(textoTurnoD);		
		// Turno E
		let turnoE=document.createElement("OPTION");
		turnoE.setAttribute("value","E");
		listaTurnos.appendChild(turnoE);
		let textoTurnoE=document.createTextNode("Turno E");
		turnoE.appendChild(textoTurnoE);			
		// console.log("Variable turno "+turnoUsuario);
		// console.log("valor lista elegido: "+listaTurnoUsuario.value);

  
		

		
 }   // fin  acciones del boton del Turno
function mostrarMenu(){
	
	let menuVisible=(menu.style.visibility=="visible");
	if (menuVisible) {
		menu.style.visibility="hidden";
	}else 	menu.style.visibility="visible";

}

function cambiarValorTurno() {
	borrarElements();
	turnoUsuario=listaTurnos.value;
	console.log(listaTurnos.value+ "y ahora turnoUsuario"+turnoUsuario);
	listaTurnos.style.visibility="hidden";
		
		crearCabecera();
		generar();
	document.body.removeChild(listaTurnos);
}

let menu=document.querySelector(".menu");

let botonMenu=document.querySelector(".conjunto");
let escuchaMenu=botonMenu.addEventListener("click",mostrarMenu);

let botonAño=document.getElementById("botonAño");
let escuchaBotonAño=botonAño.addEventListener("click",clickBotonAño);

let botonTurno=document.getElementById("botonTurno");
let escuchaBotonTurno=botonTurno.addEventListener("click",clickBotonTurno);// Pegar aqui

// let listaTurnos=document.querySelector(".listaTurnoUsuario");
// let escuchaListaTurnoUsuario=listaTurnoUsuario.addEventListener("onchange",cambiarValorTurno()) 

// FIN DE LA ESCUCHA, BORRAR SI NO VA


// calcular los dias hasta 1-1 del año que quiere ver
//diasInicioCalendario // seran los dias a sumar a 1-1 2022 para los cuales empezara un calendario posterior a 2022
let diasInicioCalendario=0;  // variable general, hay que subirla al principio
for (i=2022;i<añoUsuario;i++){
	// cambiar ubicacion funcion bisiesto....
		if (bisiesto(i)) 
			{
				diasInicioCalendario=diasInicioCalendario+366;
			}
			else{	diasInicioCalendario=diasInicioCalendario+365; }
	
	
} // fin del for de calculo de dias 



generar();
