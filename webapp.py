#!/usr/bin/python

import socket

class app:

    i = 0
    suma = 0
    error = 0
    """Application to which webApp dispatches. Does the real work

    Usually real applications inherit from this class, and redefine
    parse and process methods"""

    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information.

        request: HTTP request received from the client
        rest:    rest of the resource name after stripping the prefix
        """

        return None

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>" +
                          "Puedes hacer:\r\n| /hola || /adios || /aleat || /suma/numero |" +
                          "</h1><p></body></html>")


class webApp:
    """Root of a hierarchy of classes implementing web applications

    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def select(self, request):
        """Selects the application (in the app hierarchy) to run.

        Having into account the prefix of the resource obtained
        in the request, return the class in the app hierarchy to be
        invoked. If prefix is not found, return app class
        """

        resource = request.split(' ', 2)[1] #divido en espacios en blanco solo dos veces
        for prefix in self.apps:
            if resource.startswith(prefix):
                recurso = resource[len(prefix):]
                print ("Running app for prefix: " + prefix + \
                    ", rest of resource: " + recurso + ".")
                return (self.apps[prefix], resource[len(prefix):])
        print ("Running default app")
        return (self.myApp, resource)

    def Value_Error (self, request):
        returnCode = "400 BAD REQUEST"
        parsedRequest = request.split()[1]
        parsedRequest = parsedRequest.split('/')[2]
        print ("..ERROR..-400 BAD REQUEST-.. ResourceRcv: " + str(parsedRequest) + '\n')
        if parsedRequest == '':
            htmlAnswer = "<html><body><p><h1>"
            htmlAnswer += "La suma funciona con numeros. He recibido.. no he recibido nada. "
            htmlAnswer += "</h1></p></body></html>"
        else:
            htmlAnswer = "<html><body><p><h1>"
            htmlAnswer += "La suma funciona con numeros. He recibido: "
            htmlAnswer += str(parsedRequest)
            htmlAnswer += "</h1></p></body></html>"

        return (returnCode, htmlAnswer)

    def Index_Error (self, request):
        returnCode = "400 BAD REQUEST"
        parsedRequest = request.split()[1]
        parsedRequest = parsedRequest.split('/')[2]
        print ("..ERROR..-400 BAD REQUEST-.. ResourceRcv: " + str(parsedRequest) + '\n')
        if parsedRequest == '':
            htmlAnswer = "<html><body><p><h1>"
            htmlAnswer += "400 BAD REQUEST"
            htmlAnswer += "</h1></p></body></html>"
        else:
            htmlAnswer = "<html><body><p><h1>"
            htmlAnswer += "400 BAD REQUEST: "
            htmlAnswer += str(parsedRequest)
            htmlAnswer += "</h1></p></body></html>"

        return (returnCode, htmlAnswer)


    def __init__(self, hostname, port, apps):
        """Initialize the web application."""

        self.apps = apps #diccionario que nos pasan por parámetro
        self.myApp = app() #llamada a clase app

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)
        try:
            while True:
                print ('\nWaiting for connections..')
                (recvSocket, address) = mySocket.accept()
                print ('HTTP request received (going to parse and process):')
                request = recvSocket.recv(2048).decode("utf-8","strict")
                print (request)

                try:
                    (theApp, rest) = self.select(request)
                except IndexError:
                    print ("..ERROR..-400 BAD REQUEST-.. ResourceRcv: " + str(parsedRequest) + '\n')
                    continue

                try:
                    parsedRequest = theApp.parse(request, rest)
                except ValueError:
                    self.error = True
                    (returnCode, htmlAnswer) = self.Value_Error(request)
                    print ('Answering back...')
                    recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                                     + htmlAnswer + "\r\n", 'utf-8'))
                    recvSocket.close()
                    continue
                except IndexError:
                    self.error = True
                    (returnCode, htmlAnswer) = self.Index_Error(request)
                    print ('Answering back...')
                    recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                                     + htmlAnswer + "\r\n", 'utf-8'))
                    recvSocket.close()


                (returnCode, htmlAnswer) = theApp.process(parsedRequest)

                print ('Answering back...')
                recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                                + htmlAnswer + "\r\n", 'utf-8'))
                recvSocket.close()

        except KeyboardInterrupt:
            print (chr(27)+ "[0;31m" + "\n¡CLOSING BINDED SOCKET!" + chr(27) + "[0m")
            mySocket.close()

import hola
import aleat
import suma

if __name__ == "__main__":

    holApp = hola.holApp()
    adiosApp = hola.adiosApp()
    sumApp = suma.sumApp()
    aleatApp = aleat.aleatApp()
    testWebApp = webApp("localhost", 1234, {'/hola': holApp,
                                            '/adios': adiosApp,
                                            '/suma': sumApp,
                                            '/aleat': aleatApp})
