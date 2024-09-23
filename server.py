from socket import socket, AF_INET, SOCK_STREAM

welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(("", 5000))
welcomeSocket.listen(4)    # Max backlog 4 connections

print ('Server is listening on port 5000')
connectionSocket, addr = welcomeSocket.accept()
print ("Accept a new connection", addr)
text = connectionSocket.recv(1024).decode()
print (f"Incoming text is {text}")
connectionSocket.send(text.upper().encode())
connectionSocket.close()

welcomeSocket.close()
print("End of server")