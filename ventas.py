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


busquedaPersonalizada=consultas.vistas()
formul= cgi.FieldStorage()
elementosBusqueda=""
reportedeventa=""
band=0

try:
	nuevopasajero={'busdestino': formul['busdestino'].value ,\
	 'asiento': formul['asientodestino'].value ,\
	  'nombrepasajero': formul['pasajeroname'].value }
	g=nuevopasajero['busdestino']  
	
	elementosBusqueda22=busquedaPersonalizada.verAsientosDisponibles(g)
	for d in elementosBusqueda22:
		cadenaF="["+nuevopasajero['asiento']+"]"
		if cadenaF==d:
			band+=1
		

	if band!=0:
		busF=nuevopasajero['busdestino']
		lugarF=nuevopasajero['asiento']
		nombreF=nuevopasajero['nombrepasajero']
		reportedeventa= busquedaPersonalizada.venderLugar(busF, lugarF, nombreF)
		

	else:
		reportedeventa="El elemento que intentas ingresar no se encuentra disponible"

		
		




except Exception, e:
	print ""



###Ver lugares disponibles por bus##
try:
	datosbusqueda={'Idbus': formul['IDBus'].value }
	elementosBusqueda=busquedaPersonalizada.verAsientosDisponibles(datosbusqueda['Idbus'])

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
					$('#listado').css('text-align' , 'left');
					$('#titulo_tabla').css('margin-top' , '-8px');
					$('#Fecha_actual').css('color' , 'white');
					$('#Fecha_actual').css('text-align' , 'right');
					$('#lista_bus').css('background' , 'white');
					$('#lista_bus').css('float', 'right');
					$('#contenido').css('background', 'white');
					$('#ventas').css('width', '180px');
					$('#ventas').css('float', 'left');
					$('#ventas').css('background', 'rgb(256, 0, 51)');
					$('#ventas').css('color', 'white');
					$('#vista_buses').css('float', 'right');
					$('#vista_buses').css('width', '800px');
					$('#ventas , #vista_buses').css('display', 'inline-block');
			});

</script>

<script src="http://127.0.0.1/proyectobus/sha1.js"></script>

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


		<div id='ventas'>

			<form action="ventas.py" method="GET">
				<h2>VER LUGARES DISPONIBLES: </h2>
				
				
				<select name='IDBus'>
					"""
bBusqueda=busquedaPersonalizada.getIDBuses()

for x in bBusqueda:
	print "<option value = '"+x + "'>"+ x+" </option>"				
	

print """
</select>
<input type='submit' value='BÚSQUEDA'>
			</form>"""

print elementosBusqueda
print """
			<div id='realizarventa'>
				<h2>Realizar Venta</h2>
				<form action="ventas.py" method="POST">
					<label>Ingrese el bus destino</label>
					<select name='busdestino'>"""

bBusqueda2=busquedaPersonalizada.getIDBuses()
for s in bBusqueda2:
	print "<option value = '"+s + "'>"+ s+" </option>"				
	
print """
					</select><br>
					<label>Asiento </label>
					<input type='number' name='asientodestino'  required placeholder='numero de asiento'></input>

					<label>Nombre del pasajero</label>
					<input type='text' name='pasajeroname'  required placeholder='nombre del pasajero'></input>					

					<input type='submit'>
					
				</form>"""

print reportedeventa
print"""			</div>

		</div>	



		<div id='vista_buses'>
		<h2>listado buses</h2>
		"""
print busquedaPersonalizada.getBuses()

print """
	

	<div id='lista_bus'>
	</div>

	</body>
</html>"""
