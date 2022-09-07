import socket
host='127.0.0.1'
port=9000
s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print('Client Connected...')
while True:
    data1=c.recv(1024)
    if not data1:
        break
    print('From Clinet: ',data1.decode())
    data2=input('Enter Response = ')
    c.send(data2.encode())
c.close()
