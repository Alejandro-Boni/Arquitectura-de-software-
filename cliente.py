import socket

def main():
#crear un socket TCP
    
 client_socket=socket.socket(socket.AF_INET,socket.SOCK_SRTEAM)
#conectarse al servidor
 client_socket.connect(('127.0.0.1',12345))
 print("conectado al servidor")

#enviar los numeros a sumar 
num1=10
num2=20
data=f"{num1},{num2}".encode()
client_socket.sendall(data)

#recibir el resultado 
result=client_socket.recv(1024).decode()

#cerrar la conexion 
client_socket.close()

if__name__=='main__'
main()
