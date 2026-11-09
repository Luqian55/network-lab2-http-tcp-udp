import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(10)

s.connect(("www.bjfu.edu.cn", 80))

s.sendall(b"GET / HTTP/1.1\r\nHost: www.bjfu.edu.cn\r\nConnection: close\r\n\r\n")

data = b""

recv_sizes = []

content_length = None

while True:
    try:
        chunk = s.recv(4096)
    except socket.timeout:
        break
    if not chunk:
        break
    data += chunk
    recv_sizes.append(len(chunk))
    if content_length is None and b"\r\n\r\n" in data:
        header = data.split(b"\r\n\r\n",1)[0]

        for line in header.split(b"\r\n")[1:]:
            if line.lower().startswith(b"content-length:"):
                content_length = int(line.split(b":",1)[1].strip())
    if content_length is not None:
        body = data.split(b"\r\n\r\n",1)[1]
        if len(body) >= content_length:
            break
s.close()

print(data.decode("utf-8",errors = "replace"))
print("recv调用次数:",len(recv_sizes))
print("每次接收的字节数:",recv_sizes)