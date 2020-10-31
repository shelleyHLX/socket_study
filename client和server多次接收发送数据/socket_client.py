# coding: utf-8
# Author: shelley
# 2020/10/31,10:14
# 导入模块
import socket

# 实例初始化
client = socket.socket()
# 访问的服务器端的ip和端口
ip_port = ("127.0.0.1", 8888)
# 连接服务器
client.connect(ip_port)
# 接收主机信息，每次接收缓冲区的数据，
# 共1024字节
data = client.recv(1024)
# 打印接收的数据
# 此处的byte数据，特指python3.x以上
print(data.decode())