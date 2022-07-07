import socket

SERVER_IP = '172.20.10.7'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('Server is listening')
    s.listen(1)
    conn,addr = s.accept()
    print(f'Connection accepted from :{addr}')
    with conn:
        while(True):
            conn.send(b'Received')
            data =  conn.recv(1024)
            print(data)
            break
