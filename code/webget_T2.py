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
print("recv调用次数:",len(recv_sizes))
print("每次接收的字节数:",recv_sizes)