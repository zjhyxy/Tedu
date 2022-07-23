"""
udp客户端
"""
from socket import *
#将服务端地址设为全局变量
ADDR=('127.0.0.1',8888)
#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#消息发送接收
while True:
    msg=input(">>")
    if not msg:
        break
    sockfd.sendto(msg.encode(),ADDR)
    data,addr=sockfd.recvfrom(1024)
    print("From server:",data.decode())
#关闭套接字
sockfd.close()