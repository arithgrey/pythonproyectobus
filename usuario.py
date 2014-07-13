#!/usr/bin/python

import os
import cgi
import re

print "Content-type:text/html\r\n\r\n"
print "<html>"	
print 	"<head>"
print "</head>"
print "<body>"

Expresionm = \
re.compile( r'^\(\d{3}\)\d{3}-\d{4}$' )

formulario=cgi.FieldStorage()

try:
	datosPersonales={'elUsr': formulario['usr'].value.strip() , 'laPw': formulario['pw'].value.strip()}
	print datosPersonales['elUsr']
	print datosPersonales['laPw']
	
	
	
except KeyError:
	print "LLena los campos como se debe"
	

if Expresionm.match(datosPersonales['elUsr']):
	print Expresionm.match(datosPersonales['laPw'])
	

print "</body>"
print "</html>"
