from socket import *
server_port = 5202

server_socket = socket(AF_INET,SOCK_STREAM)

server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

server_socket.bind(("",server_port))

server_socket.listen(1)

print(f"TCP server已启动,监听端口:{server_port}")

while True:

    connection_socket,client_address = server_socket.accept()

    print(f"接受来自{client_address}的连接")

    message = connection_socket.recv(1024)

    text = message.decode("utf-8")
    
    print(f"收到消息:{text}")

    reply = f"服务器已收到:{text}"

    connection_socket.sendall(reply.encode("utf-8"))

    connection_socket.close()
    
    print("本次连接已关闭")
