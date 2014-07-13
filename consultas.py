#!/usr/bin/env python
#coding: utf8
import MySQLdb
import re

class administrador:
	def __init__(self,user, pw, mailAdmin):
		self.user=user
		self.pw=pw
		self.mailAdmin=mailAdmin


	def validacionadmin(self):
		reporte=""
		if len(self.user)<=19 and len(self.pw)<=19 and len(self.mailAdmin)<=19:

			try:
				db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
				cursor=db.cursor()
				cursor.execute("INSERT INTO  usuarios( user,  pw, mail) VALUES  ('"+self.user+"' , '"+self.pw+"' , '"+self.mailAdmin+"')")
				db.commit() #Commit es un método el cual nos permite guardar elementos en la base de datos
				db.close()
				cursor.close()
				return "ok"
			except Exception, e:
				print e
			else:
				return "Te pasaste"

class vistas:


	def insertar_bus(self, salida_hora,  destino , costo, origen, fecha_salida ):
		reporte=""

		try:
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()
			cursor.execute("INSERT INTO  bus(salida_hora,  destino , costo, origen, fecha_salida  )\
			 VALUES  ('"+salida_hora+"', '"+destino+"'  , '"+costo+"' , '"+origen+"' , '"+fecha_salida+"' )")

			db.commit()
			db.close()
			cursor.close()
			return "ok bus creado!!"
		except Exception, e:
			print e
		else:
			return "El elemento no se pudo insertar"

	def eliminar_bus(self, ID):
		try:
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()
			a=cursor.execute("delete from  bus where ID='"+ID+"' ")
			if a==0:
				return "El elemento que trato eliminar no existe!!"
				db.commit()
				db.close()
			else:
				
				db.commit()
				db.close()
				return "Ok  Bus eliminado"

		except Exception, e:
			print "No se pudo efectuar la operación"
	
	def updateBus(self, Id, destinou, fechau, horau, costou):
		try:

			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()
			# ID  | salida_hora | destino      | costo | origen | fecha_salida |
			a=cursor.execute("UPDATE bus set salida_hora='"+horau+"', destino='"+destinou+"', costo='"+costou+"', fecha_salida='"+fechau+"' \
				WHERE ID='"+Id+"' ")
			if a==0:
				
		
				db.commit()
				db.close()
				cursor.close()
				return "NO puedo efectuar cambios en el bus "

			else:
				
				db.commit()
				db.close()
				cursor.close()
				return "Ok  Bus actualizado"

		except Exception, e:
			print "No se pudo efectuar la operación"
	


		

	def eliminar_pasajero(self, ID):
		try:
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()
			a=cursor.execute("delete from pasajeros where ID='"+ID+"' ")
			if a==0:
				return "El elemento que trato eliminar no existe!!"
				db.commit()
				db.close()
			else:
				
				db.commit()
				db.close()
				return "Ok el pasajero fue eliminado correctamente"

		except Exception, e:
			print "No se pudo efectuar la operación"
				

	def getBuses(self):
		reporte=""
		try:
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()
			cursor.execute("SELECT * FROM bus")
			
			a=0
			for row in cursor:
				#ID  | salida_hora     | destino      | costo | origen | fecha_salida 
				reporte+="Bus:\t\t" + str(row[0]) + "\t\t\tSALIDA :\t\t\t " +\
				 str(row[1]) +"\t\tDESTINO: \t\t" + str(row[2])+ "\t\tPRECIO: \t\t" + str(row[3]) +"\t\tORIGEN:\t\t "+ str(row[4]) +"\t\tPARTE EL:\t\t" + str(row[5])+"<br>"
				a+=1

			reporte+="<br>Número de buses :" + str(a)
			return reporte
		except Exception, e:
			return "Problemas Al conectar la base de datos"

	def getIDBuses(self):
		try:
			arreglo=[]
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()
			cursor.execute("select ID, destino from bus")
			for x in cursor:
				busArmado=str(x[0])
				arreglo.append(busArmado)
			return arreglo	
			


		except Exception, e:
			return ""
				
	def venderLugar(self, bus , lugar, nombre):
		try:
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()
			cursor.execute("INSERT INTO pasajeros(Nombre, Asiento, Bus) VALUES ('"+nombre+"', '"+lugar+"', '"+bus+"' )")
			db.commit()
			cursor.close()
			return "OK Elemento ingresado correctamente "
			
		except Exception, e:
			return "Problemas en la base de datos"
			

	def verAsientosDisponibles(self , Id):
		try:
			Lugares=[]
			
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()  
			cursor.execute("select Asiento  from pasajeros where Bus='"+Id+"'")
			l=[]
			for x in cursor:
				l.append(x[0])
			
			cursor.close()
			l2=[]
			aa=0
			while aa<=39:
				l2.append(0)
				aa+=1

			b=0
			while b<=len(l)-1:
				l2.insert(l[b], 1)
				b+=1

			c=0
			while c<=len(l2)-1:
				if l2[c]==0:
					Lugares.append("["+str(c)+"]")
				else:
					print ""

				c+=1

			return Lugares
			
		except Exception, e:

			return e


	def getElembyBus(self, bus):	
		XX=""
		try:
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()  
			T=cursor.execute(" select pasajeros.ID, Nombre, Asiento , bus.salida_hora,\
			 destino, costo from pasajeros, bus where pasajeros.Bus=bus.ID and pasajeros.bus='"+bus+"'")

			if T!=0:

				for row in cursor:

					XX+="ID:\t\t\t\t\t "+ str(row[0]) + "\t\t\tNombre:\t\t\t "+str(row[1]) +"\t\tAsiento\t\t "+ str(row[2]) \
						+"\t\t\tsalidad de Salida:\t\t\t"+str(row[3])+"\t\t\tdestino\t\t\t"+str(row[4])+"\t\tcosto\t\t "+ str(row[5]) +"<br>"
			else:
				XX+="No Elementos en el bus indicado o el bus no existe"
									
			cursor.close()
			return XX

		except Exception, e:
			return "Problemas al conectar con la base de datos"



		

	def update_pasajero(self, ID, nombre, bus):
		try:
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()  
			T=cursor.execute("select * from pasajeros where Id='"+ID+"' and Bus='"+bus+"' ")
			if T!=0:

				cursor.execute("update pasajeros set Nombre='"+nombre+"' where ID='"+ID+"' ")
				db.commit()
				cursor.close()
				return "Elemento Actualizado correctamente!!"
			else:
				return "El usuario que decea actualizar no existe!!" 
		except Exception, e:
			return "Problemas al conectar con la base de datos"
			


	def listado_por_nombre(self, nombre):
		try:
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()
			
			cursor.execute("select pasajeros.ID, Nombre, Asiento, Bus, bus.salida_hora, destino, costo from pasajeros, bus where\
			 pasajeros.Nombre='"+nombre+"'  and pasajeros.Bus=bus.ID")
			listado="<br>"
			b=0
			for row in cursor:
				

				listado+=  "FOLIO:"+str(row[0]) +"\t\tNOMBRE:\t\t"+ str(row[1]) \
				+     "\t\tASIENTO:\t\t"+ str(row[2])+ "\t\tBUS:\t\t" +str(row[3])+ "DESTINO:"+\
				 str(row[5])+"COSTO DE VIAJE:"+ str(row[6]) +"<br>"
				b+=1
			db.close()

			if len(listado)>10:
				listado+="Número de elementos encontrados: " + str(b)
			else:
				listado+="Elemento no encontrado<br>"
			return listado

		except MySQLdb.Error, e:			
			return "Problemas al Connectar al hacer coneccion a la base de datos....."


	def verTablasCombinadas(self):
		try:
			db=MySQLdb.Connect(host="localhost", user="root", passwd="", db="sistema_bus")
			cursor=db.cursor()
			cursor.execute("select pasajeros.ID , Nombre, Asiento,  Bus, bus.destino, \
				costo from pasajeros, bus where pasajeros.Bus=bus.ID")
						
			listadoActual=""
			
			ganancias=0
			a=0
			for row in cursor:

				
				listadoActual+="Folio:\t\t"+str(row[0]) +"\t\tNombre: \t\t"+ str(row[1])\
				+"\t\tDestino:\t\t"+ str(row[4])+ "\t\t"+"Pago:"+ str(row[5])+ "\t\t\t\tAsiento: \t\t\t\t"+ str(row[2])+ \
				"\t\t\t\tBus: "+str(row[3])+ "<br>" 
				ganancias+=int(row[5])
				a+=1
				
			db.close()
			listadoActual+="<br>Número de pasajeros totales:"+ str(a) +"<br>"
			#listadoActual+="<h4>Ganancias totales: " + str(ganancias) +".00  pesos Méxicanos</h4>"

			listadoActual+="Ganancias Actuales: " + str(ganancias)+"<br><br>"
			return listadoActual

		except MySQLdb.Error, e:
			return e 
			
