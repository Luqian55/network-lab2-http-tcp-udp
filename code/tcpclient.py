from socket import *

server_name = "192.168.81.50"

server_port = 5202

client_socket = socket(AF_INET,SOCK_STREAM)

client_socket.settimeout(10)

client_socket.connect((server_name,server_port))

message = input("请输入要发送的消息:")

client_socket.sendall(message.encode("utf-8"))

reply = client_socket.recv(1024)

print(f"已收到服务器回复:{reply.decode("utf-8")}")

client_socket.close()