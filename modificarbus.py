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

formul= cgi.FieldStorage()
objbus=consultas.vistas()


T=""
try:

	datosbusqueda={'ID': formul['bus_ID_eliminar'].value}
	T+= objbus.eliminar_bus( datosbusqueda['ID'])

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
					$('h2').css('color' , '#0F878B');
					$('#Fecha_actual').css('color' , 'white');
					$('#Fecha_actual').css('text-align' , 'right');
					$('#Fecha_actual').css('margin-right' , '10px');
					$('#Fecha_actual').css('font-size' , '1.2em');
					$('#nuevo_listado').css('background' , 'white');


			});

</script>

<script src="http://127.0.0.1/proyectobus/sha1.js"></script>

</head>
<body>


<div id='contenidoHome'>
<h1 id='titulo_header'>Universidad Nacional Autónoma de México [look]</h1> 

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
"""
print "<div  id='nuevo_listado'>"
print "<h2>" + T + "</h2>"
print objbus.verBuses()


print "</div>"
print """	
		
	
	</div>
	</body>
</html>"""
