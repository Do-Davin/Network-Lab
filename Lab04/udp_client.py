from socket import *

serverName = "localhost"
serverPort = 13000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Enter message: ")
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
print("Reply from server:", modifiedSentence.decode())

clientSocket.close()