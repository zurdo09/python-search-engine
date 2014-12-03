#coding: utf-8
import re
import urllib, os
print ""

class encontrar(object):
	def pagina(self):
		respuesta = 0
		while (respuesta==0):
			while True:
				self.web=raw_input("Ingrese la primera pagina: https://")
				self.we =raw_input("Ingrese la segunda pagina: https://")
				self.pa =raw_input("Ingrese lo que desea buscar:")
				https = "https://"
				req = urllib.urlopen(https + self.web)
				r = urllib.urlopen(https + self.we)
				b = req.read()
				bb = r.read()
				p = len(re.findall(self.pa,b))
				p1 = len(re.findall(self.pa,bb))
				if p > p1:
					print "la pagina recomendada es: ",self.web
					print "cantidad de palabras encontradas: ", p
					break
				elif p == 0:
					print "palabra no encontrada"
				elif p1 ==0:
					print "palabra no encrontrada"
				else:
					print "la pagina recomendada es: ",self.we
					print "cantidad de palabras encontradas: ", p1
					
					a =	raw_input ("Desea salir? si/no ")
					b = a.lower()
					if b == "si":
						respuesta = 0
					elif b == "no":
						break
						respuesta = 1
					else:
						print "Debe ingresar una opción valida"
#c = encontrar()
p = encontrar()
#c.encontrar()
p.pagina()