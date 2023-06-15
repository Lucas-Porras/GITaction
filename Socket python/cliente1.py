import socket

socket = socket.socket()
socket.connect( ("localhost", 8000) )

mensajeCliente1 = "Hola soy el cliente 1"
socket.send(mensajeCliente1.encode("ascii"))

respuestaServer = socket.recv(1024)
print(respuestaServer)