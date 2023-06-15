import socket

socket = socket.socket()

socket.bind( ('localhost', 8000) )
socket.listen(2)

while True:
    conexionCliente1, direccion = socket.accept()
    print("Se estableció la conexión")
    print(direccion)

    mensajeCliente1 = conexionCliente1.recv(1024)
    print(mensajeCliente1)

    mensajeServidor = "Hola soy el servidor"
    conexionCliente1.send(mensajeServidor.encode("ascii"))
    conexionCliente1.close()

    #-----------------------------------------------------

    conexionCliente2, direccion = socket.accept()
    
    mensajeCliente2 = conexionCliente2.recv(2048)
    print(mensajeCliente2)

    mensajeServidor = "Hola soy el servidor"
    conexionCliente2.send(mensajeServidor.encode("ascii"))
    conexionCliente2.close()