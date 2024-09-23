from socket import socket, AF_INET, SOCK_STREAM

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))
user_input = input ("> ")
# Allocate an extensible array
b = bytearray()
b.extend(user_input.encode())
client_socket.send(b)
response = client_socket.recv(256)
text = response.decode('utf-8')
print (f'Server response {text}')