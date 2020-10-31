# coding: utf-8
# Author: shelley
# 2020/10/31,11:07
import socketserver

# 定义一个类
class MyServer(socketserver.BaseRequestHandler):
    # 执行顺序：setup, handle, finish
    # 如果handle方法出现报错，则会进行跳过
    # setup方法和finish方法无论如何都会进行执行
    def setup(self):
        pass

    def handle(self):
        # 定义连接变量
        conn = self.request
        # 发送信息定义
        msg = "Hello World!"
        # 消息发送
        conn.send(msg.encode())
        # 进入循环，不断接收客户端的消息
        while True:
            # 接收客户端的消息
            data = conn.recv(1024)
            # 打印消息
            print(data.decode())
            # 接收exit，退出
            if data == b'eixt':
                break
            #
            conn.send(data)
            import random
            conn.send(str(random.randint(1, 1000)).encode())

        conn.close()

    def finish(self):
        pass

if __name__ == '__main__':
    # 创建多线程实例
    server = socketserver.ThreadingTCPServer(
        ('127.0.0.1', 8888),
        MyServer
    )
    # 开启异步多线程，等待连接
    server.serve_forever()