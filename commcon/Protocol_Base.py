"""
@File    :   telnet_Base.py
@Modify Time
@Author       Hongrui
2024/5/11 11:10
# >>>TODO
串口、telnet、product_test(产测)
"""
import time
import json
import serial

import socket
import binascii
import telnetlib
from commcon import log_Base as lb


class MultiProtocolCommunicator:
    def __init__(self, serial_port=None, baudRate=None, telnet_ip=None, telnet_port=None, udp_ip=None,
                 udp_port=None, **kwargs):
        self.serial_port = serial_port
        self.baudRate = baudRate
        self.telnet_ip = telnet_ip
        self.telnet_port = telnet_port
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.serial_conn = None
        self.udp_sock = None
        lb.logger.info(f"连接信息：串口端口：{self.serial_port}, 波特率：{self.baudRate}，telnet地址：{self.telnet_ip}，telnet端口号：{self.telnet_port}，产测协议的地址：{self.udp_ip}, 产测协议的端口号：{self.udp_port}")


        # 打开串口
        if self.serial_port:
            self.serial_conn = serial.Serial(self.serial_port, self.baudRate, timeout=0.5)
        # 创建一个UDP对象
        self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_serial(self, message_list):
        try:
            for message in message_list:
                print('遍历列表得到：', message)
                """发送串口指令"""
                if self.serial_conn:
                    hex_message = binascii.unhexlify(message.replace(' ', ''))
                    self.serial_conn.write(hex_message)
                    print(f"串口指令已发送: {hex_message}")
                    lb.logger.info(f"串口指令已发送: {hex_message}")
                    time.sleep(0.3)
                else:
                    print("串口未初始化")

        except serial.SerialException as e:
            print(f"串口通信异常：{e}")

    # def send_telnet(self, message):
    #     """发送Telnet指令"""
    #     try:
    #         # 发起连接
    #         tn.link(self.telnet_ip, self.telnet_port)
    #         time.sleep(2)
    #         tn.login(username="admin", password="admin@123")
    #         time.sleep(2)
    #         tn.write(message.encode('ascii') + b'\n')
    #         print(f"Telnet指令已发送: {message}")
    #         # 可以添加读取响应的逻辑，这里省略
    #     except Exception as e:
    #         print(f"Telnet错误: {e}")

    @staticmethod
    def format(data):
        return data.encode('ascii') + b'\n'


    def link(self):
        # 连接设备
        self.tn = telnetlib.Telnet(self.telnet_ip, self.telnet_port, timeout=2)
        time.sleep(1)
        data = self.tn.read_very_eager().decode('UTF-8')
        print("连接结果：", data)
        lb.logger.info(f"连接结果：{data}")
        time.sleep(2)

    def login(self, username, password):
        # 发送登录信息并且监听
        # username = input("请输入账号：")
        lb.logger.info(f"获取的账号：{username}， 密码：{password}")
        self.tn.write(self.format(username))
        time.sleep(2)
        # password = input("请输入密码：")
        self.tn.write(self.format(password))
        time.sleep(2)
        data = self.tn.read_very_eager().decode('UTF-8')
        lb.logger.info(f"登录结果：{data}")
        time.sleep(2)

        # 解码返回数据
        return data

    def shell(self, command):
        # 执行命令
        self.tn.write(self.format(command))
        time.sleep(2)
        data = self.tn.read_very_eager().decode('UTF-8')
        lb.logger.info(f"执行指令结果：{data}")
        time.sleep(2)
        # 解码返回数据
        return data

    def exit(self):
        # 退出设备
        self.tn.write(self.format('exit\n'))
        # 关闭连接
        # self.tn.close()

    def send_udp(self, message, ip=None, port=None):
        """发送UDP数据包"""
        ip = ip or self.udp_ip
        port = port or self.udp_port
        # 转成json格式
        json_message = json.dumps(message)

        self.udp_sock.sendto(message.encode(), (ip, port))
        print(f"UDP数据包已发送至 {ip}:{port}: {message}")
        lb.logger.info(f"UDP数据包开始发送至 {ip}:{port}: {message}")
        self.udp_sock.settimeout(3.0)
        time.sleep(5.0) # aDm8H%MdA接收服务器的响应，设置超时时间为2秒，防止无限等待,发送查询lan口link状态时 会超时，即 超时时间设置5秒
        try:
            response = self.udp_sock.recvfrom(65507)
            lb.logger.info("发送成功")
            response_data = response[0].decode()
            lb.logger.info(f"收到的回复消息内容: {response_data}")
            lb.logger.info(f"收到的回复消息地址: {response[1]}")

        except ConnectionResetError:
            print("MDU设备已自动关闭连接，请重新发起连接")
        except socket.timeout:
            print("发送请求超时")

        return response_data

    def close(self):
        """关闭连接"""
        if self.serial_conn:
            self.serial_conn.close()
        self.udp_sock.close()


# 使用示例
if __name__ == "__main__":
    communicator = MultiProtocolCommunicator(serial_port='COM10', baudRate=9600, telnet_ip='192.168.1.1',telnet_port=23  ,udp_ip='192.168.1.1',udp_port=23)

    command_open_1 = 'A0 01 01 A2'
    command_close_1 = 'A0 01 00 A1'
    command_open_2 = 'A0 02 01 A3'
    command_close_2 = 'A0 02 00 A2'
    command_open_3 = 'A0 03 01 A4'
    command_close_3 = 'A0 03 00 A3'
    command_open_4 = 'A0 04 01 A5'
    command_close_4 = 'A0 04 00 A4'

    command_open_lsit = [command_open_1, command_open_2, command_open_3, command_open_4]
    command_close_lsit = [command_close_1, command_close_2, command_close_3, command_close_4]
    command_list = [command_open_1, command_open_2, command_open_3, command_open_4, command_close_1, command_close_2,
                    command_close_3, command_close_4]

    # 发送串口指令
    communicator.send_serial(command_open_lsit)

    # 发送Telnet指令
    communicator.send_telnet("ls -l")

    # 发送UDP数据包
    communicator.send_udp("Hello, UDP Server!")

    # 关闭连接（根据需要）