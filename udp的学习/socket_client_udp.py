# coding: utf-8
# Author: shelley
# 2020/10/31,10:57
import socket

# 定义实例
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ("127.0.0.1", 8888)
while True:
    # 输入发送的信息
    msg_input = input("请输入发送的信息：")
    # 退出的条件
    if msg_input == 'exit':
        break
    sk.sendto(msg_input.encode(), ip_port)

# 发送关闭信息
sk.close()

