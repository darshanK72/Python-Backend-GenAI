import socket

def user2():
    host = "localhost"
    port = 8999
    soc = socket.socket()
    soc.connect((host,port))

    message = input("-> ")
    while message.lower().strip() != 'bye':
        soc.send(message.encode())
        data = soc.recv(1024).decode()
        print("From User1 : ",data)
        message = input("-> ")
    
    soc.close()


user2()