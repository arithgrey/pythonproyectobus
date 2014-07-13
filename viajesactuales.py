#!/usr/bin/env python
#coding: utf8

import os
import cgi
import consultas


print "Content-type:text/html\r\n\r\n"
print "<!DOCTYPE html>"


formul= cgi.FieldStorage()
l=""
try:
	datosbusqueda={'nombre_busqueda': formul['pasajero_nombre'].value}
	
	busquedaPersonalizada=consultas.vistas()
	elementoB=datosbusqueda['nombre_busqueda']
	l= busquedaPersonalizada.listado_por_nombre(elementoB)	

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
					$('#titulo_tabla').css('margin-top' , '-10px');
					$('h2').css('color' , '#0F878B');
					$('#busqueda_dinamica').css('float' , 'right');
					$('#busqueda_dinamica').css('margin-top' , '-20px');


			});

</script>

<script src="http://127.0.0.1/proyectobus/sha1.js"></script>

</head>
<body>


<div id='contenidoHome'>
<h1 id='titulo_header'>[MY BUS.........]</h1> 


<div id='barra_navegacion'>
		<strong><ul><a href="index2.py"><li>Home</li></a></ul></strong>
					<strong><ul><a href="ventas.py"><li>Ventas</li></a></ul></strong>
					<strong><ul><a href="reportesventas.py"><li>Reportes ventas</li></a></ul></strong>
					<strong><ul><a href="bus.py"><li>Buses</li></a></ul></strong>
					<strong><ul><a href=""><li>Promociones</li></a></ul></strong>		
					<strong><ul><a href=""><li>Salir</li></a></ul></strong>

</div>




<div id="contenido">


"""		

print """
	<div id='busqueda_dinamica'>
		<h2>Busqueda dinámica</h2>
		
		<h2>Busqueda por nombre pasajero</h2>
		
		<form  id='viajesactuales.py' method="POST">
				<label>Nombre pasajero:</label>	
				<input type='text' name='pasajero_nombre' id="pasajero_nom" required></input>		
				<input type='submit' value='busqueda'/>
							
		</form>
		
		"""
print l

print """
		


	"""
print "</div>"
print "<div id='listado'>"
print "<h2 id='titulo_tabla'>Listado Global </h2>"
obj2=consultas.vistas()
print "<p>"+obj2.verTablasCombinadas()+"</p>"
print "</div>"

print """	<div id="cuenta">	

</div>

	</div>
	</div>
	</body>
</html>"""
