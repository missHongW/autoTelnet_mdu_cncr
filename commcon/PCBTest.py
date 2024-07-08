# -*- coding: utf-8 -*-
# @Time    : 2024/6/13 星期四 10:02
# @Author  : HongRui
# @File    : relay_control.py
# @Software: PyCharm
# @Comment : 继电器只能被一个控制器打开，使用时需要查看有无其他串口控制器连接

import serial
import time
import logging

class RelayController:
    def __init__(self, port, baud_rate=9600, cycle_time=2):
        self.port = port
        self.baud_rate = baud_rate
        self.cycle_time = cycle_time

        # 继电器指令（HEX形式）
        self.commands = {
            'open': [
                bytearray([0xA0, 0x01, 0x01, 0xA2]),
                bytearray([0xA0, 0x02, 0x01, 0xA3]),
                bytearray([0xA0, 0x03, 0x01, 0xA4]),
                bytearray([0xA0, 0x04, 0x01, 0xA5])
            ],
            'close': [
                bytearray([0xA0, 0x01, 0x00, 0xA1]),
                bytearray([0xA0, 0x02, 0x00, 0xA2]),
                bytearray([0xA0, 0x03, 0x00, 0xA3]),
                bytearray([0xA0, 0x04, 0x00, 0xA4])
            ],
            'status': bytearray([0xFF])
        }

    def control_relay(self):
        try:
            with serial.Serial(self.port, self.baud_rate, timeout=1) as ser:
                # logging.info('串口打开成功')

                while True:
                    # 关闭所有继电器
                    for cmd in self.commands['close']:
                        ser.write(cmd)
                        time.sleep(0.1)  # 确保每个指令之间有足够的时间传输

                    logging.info("所有继电器已关闭")
                    time.sleep(self.cycle_time)  # 等待指定的周期时间

                    # 打开所有继电器
                    for cmd in self.commands['open']:
                        ser.write(cmd)
                        time.sleep(0.1)  # 确保每个指令之间有足够的时间传输

                    logging.info("所有继电器已打开")
                    time.sleep(self.cycle_time)  # 等待指定的周期时间

                    ser.write(self.commands['status'])
                    status = ser.readall().strip()
                    logging.info(f"继电器状态: {status}")
                    time.sleep(1)

        except serial.SerialException as e:
            logging.error(f'打开串口失败：{e}')
        except Exception as e:
            logging.error(f"发生错误：{e}")

# 示例使用
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    port = 'COM11'  # 替换为实际的串口号
    cycle_time = 5  # 设置继电器开关的周期等待时间（秒）

    relay_controller = RelayController(port, cycle_time=cycle_time)
    relay_controller.control_relay()
