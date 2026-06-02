import socket
def user1():
    host = "localhost"
    port = 8999
    soc = socket.socket()
    soc.bind((host,port))
    soc.listen(2)
    conn,addr = soc.accept()
    print("Connected To : ",addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From User2 : ",data)
        data = input("-> ")
        conn.send(data.encode())
    
    conn.close()

user1()