from socket import *

server_name = "192.168.81.50"
server_port = 5201

import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "payload_2000.bin"
)

with open(file_path, "rb") as f:
    data = f.read(2000)

print("发送字节数:", len(data))

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(5)

client_socket.sendto(data, (server_name, server_port))

try:
    reply, server_address = client_socket.recvfrom(2048)
    print("收到服务器回复:", reply.decode("utf-8"))
except TimeoutError:
    print("等待服务器回复超时")

client_socket.close()