# coding: utf-8
# Author: shelley
# 2020/10/31,11:33
import socket
"""
服务端
"""
# 实例化
sk = socket.socket()
# 定义连接ip
ip_port = ("127.0.0.1", 9999)
# 绑定ip和port
sk.bind(ip_port)
# 最大连接数
sk.listen(5)
# 进入循环接收数据
while True:
    # 等待客户端连接
    conn, address = sk.accept()
    while True:
        # 一直使用当前连接进行数据发送
        # 直到结束标志出现
        # 打开文件，等待数据写入
        with open('file', "ab") as f:
            # 接收数据
            data = conn.recv(1024)
            if data == b'quit':
                break
            # 写入文件
            f.write(data)
        # 接收完成标志
        # conn.send('success'.encode())
    # 关闭连接
    sk.close()

# 服务器接收到第一条数据，
# 客户端发送完所有数据，数据在缓冲区中
# ，quit也当做数据写入。
