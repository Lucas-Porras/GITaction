import socket

socket = socket.socket()
socket.connect( ("localhost", 8000) )

mensajeCliente2 = "Hola soy el cliente 2"
socket.send(mensajeCliente2.encode("ascii"))

respuestaServer = socket.recv(2048)
print(respuestaServer)