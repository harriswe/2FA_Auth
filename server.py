import math
import random
import threading
from socket import socket, AF_INET, SOCK_STREAM

def many_clients():

    welcomeSocket = socket(AF_INET, SOCK_STREAM)
    welcomeSocket.bind(("", 9000))
    welcomeSocket.listen(4)    # Max backlog 4 connections
    print('Server is listening on port 9000')
    while True:
        connectionSocket, addr = welcomeSocket.accept()
        client_thread = threading.Thread(target=many_clients, args=(connectionSocket,))
        client_thread.start()

        print(f"Accepted connection from {addr}")
        print("Accept a new connection", addr)
        text = connectionSocket.recv(1024).decode()

        if not text:
            break

        print(f"Incoming text is {text}")
        seed = str(random.randint(100000, 400000))
        print(f"Seed is {seed}")
        print("Sending seed and initial response...")
        connectionSocket.send(seed.encode())
        connectionSocket.send("Please enter a password meeting the following criteria: six digit numeric"
                              "followed by a word and special character.".encode())

        # Listens for password sent.
        token, password = connectionSocket.recv(1024).decode().split(' ', 1)
        handle_client(connectionSocket, token, password, seed)


        finally: connectionSocket.close()

        welcomeSocket.close()
        print("End of server")


def handle_client(connectionSocket, token, password, seed):


        if token.len() < 6:
            connectionSocket.send("404 Numeric code is not 6-digit")
        elif token + password == len(token) or len(password) < 1:
            connectionSocket.send("401 Not enough token")
        elif not token.isdigit():
            connectionSocket.send("403 Missing numeric code")
        elif int(token) < int(seed):
            connectionSocket.send("402 Numeric code less than seed")
        elif sum(int(digit) for digit in token) % 2 == 1:
            connectionSocket.send("405 Wrong password")
        else:
            connectionSocket.send("200 Password Accepted")



