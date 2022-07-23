"""
    http测试
"""
from socket import *
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8000))
s.listen(3)
c,addr=s.accept()
print("Connect from",addr)
data=c.recv(2048)
print(data.decode())
data="""HTTP/1.1 200 ok
Content_Type:text/html

<h1>hello world<h1>
"""
c.send(data.encode())
c.close()
s.close()