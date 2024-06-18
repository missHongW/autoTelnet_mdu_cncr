# -*- coding: utf-8 -*-
# @Time    : 2024/6/17 下午2:05
# @Author  : HongRui
# @File    : Reboot.py
# @Software: PyCharm
# @Comment :

import telnetlib
from commcon import Telnet_Link as tb
from commcon import log_Base as lb

class Reboot_Device:

    def reboot_device(self):
        tl = tb.TelnetLib()
        tl.link('192.168.1.1')
        print(">>>登录设备")
        lb.logger.info(">>>登录设备")
        tl.login("admin", 'aDm8H%MdA')
        tl.shell("su")
        tl.shell("aDm8H%MdA")
        res = tl.shell("sidbg 1 DB reset")
        print(f"执行指令恢复出厂中...{res}")
        lb.logger.info(f"执行指令恢复出厂中...{res}")

    def verify_device(self, www):
        tl = tb.TelnetLib()
        tl.link('192.168.1.1')
        tl.login("admin", 'aDm8H%MdA')
        tl.shell("su")
        tl.shell("aDm8H%MdA")
        res = tl.shell("ping "+www)
        print(f"执行指令结果：{res}")
        lb.logger.info(f"执行指令结果：{res}")

if __name__ == "__main__":
    rd = Reboot_Device()
    rd.verify_device(www="www.taobao.com")
    rd.reboot_device()
