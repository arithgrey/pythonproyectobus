#!/usr/bin/env python
#coding: utf8

import os
import cgi

print "Content-type:text/html\r\n\r\n"
print "<!DOCTYPE html>"
print """<html>
<head>
<title> Sistema de buses por Medrano Salazar jonathan UNAM</title>
<link rel='stylesheet' type='text/css' href='http://127.0.0.1/proyectobus/estilosbase.css'>

<script src='http://localhost/proyectobus/jquery-1.9.1.min.js'></script>	
		<script type="text/javascript">
			
			$(document).on('ready', function(){

					$('body').css('font-family', 'sans-serif','ubuntu', 'Comic Sans');
					$('#cuenta').css('margin-top', '-160px');
					$('#cuenta').css('float', 'right');
					$('#contenido').css('background', 'white');
					$('h2').css('color', 'rgb(1, 125, 155)');

			});

</script>

<script src="http://127.0.0.1/proyectobus/sha1.js"></script>
<script type="text/javascript">
		
		function getCifrado(){


			var usuarioLogg=document.getElementById("nuevoUsuario").value;
			var passTT=document.getElementById("contraNuevoUser").value;
			var nuevoMail=document.getElementById("mailNuevo").value;

			var usrcrip = CryptoJS.SHA1(usuarioLogg);
			var passTTC= CryptoJS.SHA1(passTT);
			var nuevoMailC= CryptoJS.SHA1(nuevoMail);

		}

 </script>



</head>
<body>


<div id='contenidoHome'>
<h1 id='titulo_header'>[MY BUS.........]</h1> 



<div id='barra_navegacion'>
		
					<strong><ul><a href="index2.py"><li>Home</li></a></ul></strong>
					<strong><ul><a href="ventas.py"><li>Ventas</li></a></ul></strong>
					<strong><ul><a href="reportesventas.py"><li>Reportes ventas</li></a></ul></strong>
					<strong><ul><a href="bus.py"><li>Buses</li></a></ul></strong>
					<strong><ul><a href=""><li>promociones</li></a></ul></strong>

</div>




<div id="contenido">

		<h2>Acceder</h2>
		<form id='formularioLog' method="POST" action="usuario.py">

				<label>Usuario:</label></br>
				<input type='text' name='usr' id="usuarioLog" placeholder='Usuario' required ></input></br>
				<label>Password:</label></br>
				<input type='password' name="pw"  id="passLog" required></input></br>
				<button>Ingresar</button></br>
		</form>

"""		
	
	
		


print """	<div id="cuenta">
	
			<h2>Nuevo Administrador</h2>
			<form id='formNuevaCuenta' method='POST' action='cuentasactuales.py'>
				<label>Usuario:</label></br>
				<input type='text' name='nuevousuario' id="nuevoUsuario" placeholder='Tu usuario' required ></input></br>
				<label>Password:</label></br>
				<input type='password' name='nuevapass' id="contraNuevoUser" required></input></br>
				<label>Correo Electrónico</label></br>
				<input type='email' name='nuevomail' id="mailNuevo" placeholder='arithgrey@hotmail.com' required></input></br>
				
				<button onclick="getCifrado()">Crear cuenta</button>

		</form>


</div>

	</div>
	</div>
	</body>
</html>"""
