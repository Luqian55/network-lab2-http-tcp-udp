from socket import *
server_port = 5201

server_socket = socket(AF_INET,SOCK_DGRAM)

server_socket.bind(("",server_port))

print(f"UDP server 已启动,监听端口:{server_port}")

while True:

    message,client_address = server_socket.recvfrom(2048)

    text = message.decode("utf-8")

    print(f"收到来自{client_address}的消息:{text}")

    reply = f"服务器已收到{text}"

    server_socket.sendto(reply.encode("utf-8"),client_address)

