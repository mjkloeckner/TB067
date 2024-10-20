from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print(f'Listening on port {serverPort}')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(f'Received message from {clientAddress[0]}')
    print("Converting message to upper case...")
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print(f'Replied sent to {clientAddress[0]}:{clientAddress[1]}')
