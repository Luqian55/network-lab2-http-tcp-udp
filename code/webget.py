import socket
import sys

# GitHub 公有仓库：
# https://github.com/Luqian55/network-lab2-http-tcp-udp

if len(sys.argv) < 3:
    print("用法: python webget.py host path [port]")
    sys.exit(1)

host = sys.argv[1]
path = sys.argv[2]
port = int(sys.argv[3]) if len(sys.argv) >= 4 else 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect((host, port))

request = (
    f"GET {path} HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Connection: close\r\n"
    "\r\n"
)

s.sendall(request.encode("ascii"))

data = b""
recv_sizes = []
content_length = None

# TCP 是字节流，一次 recv 不保证收到完整响应。
# 结束条件只有两种：收够 Content-Length，或对端关闭后 recv 返回空字节。
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
        header = data.split(b"\r\n\r\n", 1)[0]

        # 响应头存在 Content-Length 时，按其指定长度判断正文是否收完。
        for line in header.split(b"\r\n")[1:]:
            if line.lower().startswith(b"content-length:"):
                content_length = int(line.split(b":", 1)[1].strip())

    if content_length is not None:
        body = data.split(b"\r\n\r\n", 1)[1]
        if len(body) >= content_length:
            break

s.close()

header, body = data.split(b"\r\n\r\n", 1)
header_text = header.decode("iso-8859-1")
header_lines = header_text.split("\r\n")

status_line = header_lines[0]
status_code = status_line.split(" ")[1]

print("状态行:", status_line)
print("状态码:", status_code)
print("响应头:")

for line in header_lines[1:]:
    print(line)

with open("output.bin", "wb") as f:
    f.write(body)

print("body已保存:", len(body), "字节")
print("recv调用次数:", len(recv_sizes))
print("每次接收字节数:", recv_sizes)
