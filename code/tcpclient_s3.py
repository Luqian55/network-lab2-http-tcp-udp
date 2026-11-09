from socket import *
import os
import time

server_name = "192.168.81.50"
server_port = 5202

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
client_socket.sendall("hello s3".encode("utf-8"))

reply = client_socket.recv(1024)
print("收到回复:", reply.decode("utf-8"))
print("client PID:", os.getpid(), flush=True)
print("保持连接中，请强制结束本进程", flush=True)

time.sleep(300)