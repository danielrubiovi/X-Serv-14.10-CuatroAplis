#!/usr/bin/python

import socket
import webapp

class sumApp(webapp.app):

	def parse (self,request,rest):
		
		numero = request.split()[1]
		numero = int(numero.split('/')[2])
		print("NumeroRcv: " + str(numero))
		return numero

	def process (self, parsedRequest):
		if self.i == 0 or self.i == 1:
			if self.i == 0:
				msg = 'Primer numero recibido: ' + str(parsedRequest)
				msg += '. Dame otro numero.'
				self.suma = self.suma + parsedRequest
			if self.i == 1:
				msg = 'Segundo numero recibido: ' + str(parsedRequest)
				msg += '. La suma de ' + str(self.suma) + ' + '
				msg += str(parsedRequest) + ' es '
				self.suma = self.suma + parsedRequest
				msg += str(self.suma)
			self.i = self.i + 1
		elif self.i >= 2:
			self.suma = 0
			self.i = 0
			msg = 'Primer numero recibido: ' + str(parsedRequest)
			msg +='. Dame otro numero.\n'
			self.suma = self.suma + parsedRequest
			self.i = self.i + 1

		print ("Suma: " + str(self.suma))
		print("I: " + str(self.i))

		if not self.error:
			htmlAnswer = "<html><body><p><h1>"
			htmlAnswer += str(msg)
			htmlAnswer += "</h1></p></body></html>"
		else:
			htmlAnswer = "<html><body><p><h1>"
			htmlAnswer += "ERROR"
			htmlAnswer += "</h1></p></body></html>"

		return ("200 OK", htmlAnswer)

#if __name__ == "__main__":
	#sumApp = sumApp()
	#testWebApp = webapp.webApp("localhost", 1234, {'/suma': sumApp,})