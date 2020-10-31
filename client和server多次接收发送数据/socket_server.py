# coding: utf-8
# Author: shelley
# 2020/10/31,10:06
import socket

# 创建实例
sk = socket.socket()
# 定义绑定ip和port
ip_port = ("127.0.0.1", 8888)
# 绑定监听
sk.bind(ip_port)
# 最大连接数
sk.listen(5)
# 提示信息
print("正在进行等待接收数据......")
# 接收数据
conn, address = sk.accept()
# 定义信息
msg = "Hello World"
# 返回信息
# python3.x以上，网络数据的发送接收都是byte类型
# 如果发送的数据是str型，则需要进行编码
# 发送的数据存在缓冲区中
conn.send(msg.encode())
conn.close()


