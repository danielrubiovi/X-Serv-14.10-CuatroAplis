#!/usr/bin/python

import webapp
import random

class holApp(webapp.app):

    def parse(self,request,rest):

        num_random = str(random.randrange(1001))
        return num_random

    def process(self, parsedRequest):

        imagen_suerte = 'http://ismaelru-cp193.wordpresstemporal.com/wp-content/uploads/2016/03/2879272005-0f2bf7e96a-1-300x200.jpg'
        imagen_hell = 'http://www.disfrazmania.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/d/i/disfraz-de-demonio-de-lujo-31937.jpg'
        print ('Numero_randomRcv: ' + str(parsedRequest))
        if int(parsedRequest) <= 250:
            htmlAnswer = "<html><body><h1>"
            htmlAnswer += "Holaaa :)"
            htmlAnswer += "</h1></body></html>"
        elif int(parsedRequest) > 250 and int(parsedRequest) <= 500:
            htmlAnswer = "<html><body><h1>"
            htmlAnswer += "Hola. Que haces?"
            htmlAnswer += "</h1></body></html>"
        elif int(parsedRequest) == 666:
            htmlAnswer = "<html><body><h1>"
            htmlAnswer += "Hola. Este mensaje sale solo a los.. <p style= 'color:red'>BAD BOY's</p>"
            htmlAnswer += "<p><IMG SRC=" + imagen_hell + "></p>"
            htmlAnswer += "</h1></body></html>"
        elif int(parsedRequest) > 500 and int(parsedRequest) <= 985:
            htmlAnswer = "<html><body><h1>"
            htmlAnswer += "Hola."
            htmlAnswer += "</h1></body></html>"
        elif int(parsedRequest) > 985 and int(parsedRequest) <= 1000:
            htmlAnswer = "<html><body><h1>"
            htmlAnswer += "<p style= 'color:green'> Hola. Hoy es tu dia de suerte!</p>"
            htmlAnswer += "<p> TENIAS SOLO UN 0,014% DE PROBABILIDAD DE VER ESTE MENSAJE!!! </p>"
            htmlAnswer += "<p style= 'color:blue'> Enhorabuena!</p>"
            htmlAnswer += "<p><IMG SRC=" + imagen_suerte + "></p>"
            htmlAnswer += "</p></h1></body></html>"
        return ("200 OK", htmlAnswer)

class adiosApp(webapp.app):

    def process(self, parsedRequest):
        htmlAnswer = "<html><body><h1>"
        htmlAnswer += "Adios."
        htmlAnswer += "</h1></body></html>"
        return ("200 OK", htmlAnswer)

#if __name__ == "__main__":
 #   holApp = holApp()
  #  adiosApp = adiosApp()
   # testWebApp = webapp.webApp("localhost", 1234, {'/hola': holApp,
    #                                    '/adios': adiosApp,})
