#!/usr/bin/env python
#coding: utf8

import os
import cgi
import consultas


from datetime import datetime
today = datetime.now()
Fecha= str(today.day)+"/" + str(today.month) +"/"+ str(today.year)



print "Content-type:text/html\r\n\r\n"
print "<!DOCTYPE html>"


vistaglobal=consultas.vistas() #Objeto global para las consultas

formul= cgi.FieldStorage()

l=""
S=""
updateS=""
busquedaPorBus=""

try:
	datosbus={'bus_busqueda': formul['numerodebus'].value}
	busquedaPorBus=vistaglobal.getElembyBus(datosbus['bus_busqueda'])
	
except Exception, e:
	print ""


	

try:
	datos_update={'Id': formul['Id_update'].value, 'nom': formul['nombre_update'].value, 'bus': formul['bus_update'].value}
	updateS= vistaglobal.update_pasajero(datos_update['Id'], datos_update['nom'], datos_update['bus'])


except Exception, e:
	print ""
	

##Recibe el Id del elemento a eliminar 
try:
	elemento_a_eliminar={'id':formul['nombre_eliminar'].value}
	S+=vistaglobal.eliminar_pasajero(elemento_a_eliminar['id'])
	
except Exception, e:
	print ""


##recibe datos mandados desde el formulario búsqueda y realiza sus labores correspondientes 
try:
	datosbusqueda={'nombre_busqueda': formul['pasajero_nombre'].value}
	elementoB=datosbusqueda['nombre_busqueda']
	l=vistaglobal.listado_por_nombre(elementoB)	

except Exception, e:
	print ""


print """<html>
<head>
<title> Sistema de buses por Medrano Salazar jonathan UNAM</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel='stylesheet' type='text/css' href='http://127.0.0.1/proyectobus/estilosbase.css'>

<script src='http://localhost/proyectobus/jquery-1.9.1.min.js'></script>	
		<script type="text/javascript">
			
			$(document).on('ready', function(){

					$('body').css('font-family', 'sans-serif','ubuntu', 'Comic Sans');
					$('#busqueda_por_nombre').css('background' , 'rgb(59,106,111)');
					$('#Fecha_actual').css('color', 'white');
					$('#del').css('background' , 'grey');
					$('#del').css('color' , 'white');
					$('#update').css('background' , 'rgb(12,196,131)');
					$('#update').css('color' , 'white');
					$('#busqueda_por_bus').css('background' , 'rgb(165, 88, 81)');
					$('#busqueda_por_nombre,  #del, #update, #busqueda_por_bus ').css('display', 'inline-block');
					$('#busqueda_por_nombre,  #del, #update, #busqueda_por_bus ').css('text-align', 'center');
					$('#busqueda_por_nombre,  #del, #update, #busqueda_por_bus ').css('width', '200px');
					$('#busqueda_por_nombre,  #del, #update, #busqueda_por_bus ').css('color', 'white');
					$('#Listado_Global').css('text-align', 'center');
					$('#Listado_Global').css('color', 'white');
					$('#busqueda_por_bus').css('margin-top' , '50px');
					$('#estados').css('background', 'white');
					$('#contenido').css('background', 'white');
					$('#Fecha_actual').css('float', 'right' );
			});

</script>

</head>
<body>


<div id='contenidoHome'>
<h1 id='titulo_header'>[MY BUS.........]</h1> 

"""
print  "<strong><p id='Fecha_actual'>" +  Fecha  + "</p></strong>"
print """
			<div id='barra_navegacion'>
					

					<strong><ul><a href="index2.py"><li>Home</li></a></ul></strong>
					<strong><ul><a href="ventas.py"><li>Ventas</li></a></ul></strong>
					<strong><ul><a href="reportesventas.py"><li>Reportes ventas</li></a></ul></strong>
					<strong><ul><a href="bus.py"><li>Buses</li></a></ul></strong>
					<strong><ul><a href=""><li>Promociones</li></a></ul></strong>		
					<strong><ul><a href=""><li>Salir</li></a></ul></strong>


			</div>

<div id="contenido">

	<div id='busqueda_por_nombre'>
				
		<h2>Búsqueda de pasajeros <br>por nombre </h2>
		<form  id='ventas.py' method="POST">
				<label>Nombre pasajero:</label>	
				<input type='text' name='pasajero_nombre' id="pasajero_nom" required placeholder='Rakel'></input>		
				<input type='submit' value='búsqueda'/>
		</form>
	</div>	


	<div id='del'>
		<h2>Cancelar venta</h2>

			<form action='reportesventas.py' method='POST'>
				
				<label> Ingresé 
				el folio de venta</label>
				<input type='number' name='nombre_eliminar' placeholder='23'>
				<input type='submit' value='Cancelar venta'>
			</form>
	</div>

	<div id='update'>
		<h2>Actualizar datos <br> del usuario</h2>

			<form action='reportesventas.py' method='POST'>
				<br>
				<label>Ingresé el folio
				<br>del elemento a actualizar</label>

				<input type='number' name='Id_update' placeholder='24' required>

				
				<label>Autobus del elemeto a actualizar</label>
				<input type='number' name='bus_update' placeholder='24'>

				<label>Nuevo nombre</label>
					<input type='text' name='nombre_update' placeholder='arith' required>
				

				<input type='submit' value='Actualizar'>
			</form>
	</div>

	<div id='busqueda_por_bus'>
		<h2>Ver pasajeros por bus:</h2>
		<form action='reportesventas.py' method='POST'>
			<input text='number' name='numerodebus' required placeholder='Número de bus'></input>
			<input type='submit' value='buscar por bus'></input>
		</form>
	</div>

	</div>
	



	<div id='estados'>
"""
print S
print l
print updateS
print busquedaPorBus

print """
	</div>


	<div id='Listado_Global'>
		<h1>Listado Global</h1>
"""

print vistaglobal.verTablasCombinadas()
print """
	</div>






	</div>
</body>
</html>"""
