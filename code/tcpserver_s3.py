from socket import *

import time

server_port = 5202

server_socket = socket(AF_INET,SOCK_STREAM)

server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

server_socket.bind(("",server_port))

server_socket.listen(1)

print("s3 server已启动",flush = True)

connection_socket,client_address = server_socket.accept()

print("客户端已连接:",client_address,flush=True)

while True:
    try:
        data = connection_socket.recv(1024)
    except ConnectionReseError:
        print("服务器收到RST",flush = True)
        break

    if not data:
        print("服务器收到FIN，连接进入CLOSE_WAIT",flush=True)
        time.sleep(180)
        break

    text = data.decode("utf-8")
    print("收到:",text,flush = True)
    connection_socket.sendall(f"服务器已收到：{text}".encode("utf-8"))

connection_socket.close()

server_socket.close()
