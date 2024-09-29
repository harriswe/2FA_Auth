import random
import threading
from socket import socket, AF_INET, SOCK_STREAM

def handle_client_connection(connectionSocket):
    try:
        print(f"Accepted connection.")
        text = connectionSocket.recv(1024).decode()

        if not text:
            return

        print(f"Incoming text is {text}")
        seed = str(random.randint(100000, 400000))
        print(f"Seed is {seed}")
        print("Sending seed and initial response...")
        connectionSocket.send(seed.encode())
        connectionSocket.send("Please enter a password meeting the following criteria: six digit numeric followed by a word and special character.".encode())

        # Listens for password sent.
        token, password = connectionSocket.recv(1024).decode().split(' ', 1)
        handle_client(connectionSocket, token, password, seed)

    finally:
        connectionSocket.close()


def many_clients():
    try:
        welcomeSocket = socket(AF_INET, SOCK_STREAM)
        welcomeSocket.bind(("", 9000))
        welcomeSocket.listen(4)    # Max backlog 4 connections
        print('Server is listening on port 9000')

        while True:
            connectionSocket, addr = welcomeSocket.accept()
            client_thread = threading.Thread(target=handle_client_connection, args=(connectionSocket,))
            client_thread.start()

    finally:
        welcomeSocket.close()
        print("End of server")


def handle_client(connectionSocket, token, password, seed):
    try:
        if len(token) < 6:
            connectionSocket.send("404 Numeric code is not 6-digit".encode())
        elif token + password == len(token) or len(password) < 1:
            connectionSocket.send("401 Not enough token".encode())
        elif not token.isdigit():
            connectionSocket.send("403 Missing numeric code".encode())
        elif int(token) < int(seed):
            connectionSocket.send("402 Numeric code less than seed".encode())
        elif sum(int(digit) for digit in token) % 2 == 1:
            connectionSocket.send("405 Wrong password".encode())
        else:
            connectionSocket.send("200 Password Accepted".encode())
    finally:
        connectionSocket.close()