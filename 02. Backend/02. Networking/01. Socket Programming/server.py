import socket

server = socket.socket()

server.bind(("localhost",8999))

server.listen(1)

while True:
    conn,addr = server.accept()
    print("Conncted To : ",addr)
    conn.send(bytes("Welcome to Server",'utf-8'))
    conn.close()