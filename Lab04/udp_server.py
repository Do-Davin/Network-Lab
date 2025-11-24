from socket import *

serverPort = 13000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("TCP server is ready to receive")

while True:
    connectionSocket, clientAddress = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalized = sentence.upper()
    connectionSocket.send(capitalized.encode())
    connectionSocket.close()