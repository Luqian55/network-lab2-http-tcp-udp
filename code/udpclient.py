from socket import*

server_name = "192.168.81.50"

server_port = 5201

client_socket = socket(AF_INET,SOCK_DGRAM)

client_socket.settimeout(5)

message = input("请输入要发送的消息:")

client_socket.sendto(
    message.encode("utf-8"),
    (server_name,server_port)
)

try:
    reply,server_address = client_socket.recvfrom(2048)
    print(f"收到来自{server_address}的回复:")
    print(reply.decode("utf-8"))
except TimeoutError:
    print("等待服务器回复超时")    

client_socket.close()    