"""
@File    :   telnet_Base.py   
@Modify Time      
@Author       wujie 
2024/4/26 16:10      
# >>>TODO

执行telnet指令的基类
连接Telnet
登录
发送telnet指令
"""

import telnetlib
import time


class TelnetLib(object):

    def __init__(self):
        self.tn = None
        self.EXIT = b'quit\n'
        self.LOGIN = b'Login'
        self.USERNAME = b'Username:'
        self.PASSWORD = b'Password:'

    @staticmethod
    def format(data):
        return data.encode('ascii') + b'\n'

    def link(self, host, port=23, timeout=3):
        # 捕获连接异常
        try:
            # 连接设备
            self.tn = telnetlib.Telnet(host, port, timeout)
            time.sleep(2)
            data = self.tn.read_very_eager().decode('UTF-8')
            return data


        except ConnectionRefusedError:
            print("连接失败，可能是web配置后台未启用Telnet配置")

        else:
            print('连接成功,输入账号')
        finally:
            pass




    def login(self, username, password):
        # 发送登录信息并且监听
        # username = input("请输入账号：")
        self.tn.write(self.format(username))
        time.sleep(2)
        # password = input("请输入密码：")
        self.tn.write(self.format(password))

    def shell(self, command):
        # 执行命令
        self.tn.write(self.format(command))
        time.sleep(1)
        data = self.tn.read_very_eager().decode('UTF-8')
        # 解码返回数据
        return data

    def exit(self):
        # 退出设备
        self.tn.write(self.format('exit\n'))
        # 关闭连接
        # self.tn.close()


if __name__ == '__main__':
    tl = TelnetLib()
    print(tl.link('192.168.1.1'))
    # tl.login('admin', 'admin@123')
    # mdu_res = tl.shell(command='ls')

    # print(mdu_res+"12")
