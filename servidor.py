import socket 

def main():
#crear un socket TCP
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#vincular el socket a una direccion y puerto especifico
server_socket.bind(('0.0.0.0',12345))
#escuchar conexiones entrantes 
server_socket.listen(1)
print("Servidor escuchando el puerto 12345")

While True:
#aceptar conecciones entrantes
client_socket,client_address=server_socket.accept()
print(f"coneccion entrande de {client_address}")
#recibir datos del cliente
data=client_socket.recv(1024)
num1,num2=map(int,data.decode().split(,))

#calcular la suma 
result=num1+num2

#enviar el resultado al cliente
client_socket.sendall(str(result).encode())

#cerrar conexion
client_socket.close()

if__name__=='__main__':
main()
