#!usr/bin/python
####CORREGIR QUE SIGA PIDIENDO COSITAS ALEATORIAS
import webapp
import random

class aleatApp(webapp.app):

    def process(self,parsedRequest):
        num_random = str(random.randrange(1000))
        url = 'http://localhost:1234/aleat/'
        htmlAnswer = "<html><body>"
        htmlAnswer += "<p><h2>" + "Hola. " + "</h2></p>"
        htmlAnswer += "<h4><a href=" + url + num_random + ">Dame numero aleatorio.</a></h4>"
        htmlAnswer += "</body></html>"
        return("301 MOVED PERMANENTLY", htmlAnswer)