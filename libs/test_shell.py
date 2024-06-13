"""
@File    :   test_link.py   
@Modify Time      
@Author       wujie 
2024/4/29 15:57      
# >>>TODO 连接Telnet
"""

import pytest
import allure
import sys
from utils import handle_yaml
from commcon import Telnet_Link as tb
from commcon import log_Base as lb

@allure.epic('MDU-Test')
@allure.feature('发送Telnet指令')
class TestShell:

    def setup_class(self):
        self.tl = tb.TelnetLib()
        self.tl.link(handle_yaml.get_yaml_data()['Link']['ip'])
        self.tl.login(handle_yaml.get_yaml_data()['Login']['username'],
                      handle_yaml.get_yaml_data()['Login']['password'])
        lb.logger.info(f"setup_class运行了")

    @pytest.fixture()
    def shell(self, request):
        return request.param

    @allure.story("Telnet")
    @allure.title("查看目录文件")
    @pytest.mark.parametrize('shell', [handle_yaml.get_yaml_data()['Shell']], indirect=True)
    def test_shell_ls(self, shell):
        lb.logger.info(f"{__name__, sys._getframe().f_code.co_name}>>>>>发送指令信息:{shell}")
        lb.logger.info(f"test_shell_ls 方法解包shell['doc']>>>>>{shell['doc']}")
        re = self.tl.shell(shell['doc'])
        lb.logger.info(f"test_shell_ls 方法运行后的结果：>>>>>{re}")
        assert shell['expect'][0] == re

    @allure.story("Telnet")
    @allure.title("查看设备mac信息")
    @pytest.mark.parametrize('shell', [handle_yaml.get_yaml_data()['Shell']], indirect=True)
    def test_shell_mac(self, shell):
        lb.logger.info(f"{__name__, sys._getframe().f_code.co_name}>>>>>发送指令信息:{shell}")
        lb.logger.info(f"test_shell_ls 方法解包shell['doc']>>>>>{shell['mac']}")
        re = self.tl.shell(shell['mac'])
        lb.logger.info(f"test_shell_ls 方法解包shell['doc']>>>>>{shell['mac']}")
        lb.logger.info(f"test_shell_mac 方法运行后的结果：>>>>>{re}")
        assert shell['expect'][1] in re




    def teardown_class(self):
        self.tl.exit()


if __name__ == '__main__':
    pytest.main()
