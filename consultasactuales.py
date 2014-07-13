#!/usr/bin/env python
#coding: utf8

import os
import cgi
import re
import consultas

print "Content-type:text/html\r\n\r\n"
print "<html>"	
print 	"<head>"
print "</head>"
print "<body>"

Expresionm = \
re.compile( r'^\(\d{3}\)\d{3}-\d{4}$' )

formulario=cgi.FieldStorage()

try:
	
	datosUsuario={'usr': formulario['nuevousuario'].value , 'contras': formulario['nuevapass'].value , 'correo': formulario['nuevomail'].value}
	print datosUsuario['usr']
	print datosUsuario['contras']
	print datosUsuario['correo']

	print "<br>"	

	obj=consultas.administrador(datosUsuario['usr'] , datosUsuario['contras'] , datosUsuario['correo'])
	print obj.validacionadmin()
	
except KeyError:
	print "Campos invalidos"
	


print "</body>"
print "</html>"
}
##permisoss 755##
