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
from commcon import telnet_Base as tb
from commcon import log_Base as lb

@allure.epic('MDU-Test')
@allure.feature('登录Telnet')
class TestLogin:

    def setup_class(self):
        self.tl = tb.TelnetLib()
        self.tl.link(handle_yaml.get_yaml_data()['Link']['ip'])

    @pytest.fixture()
    def login(self, request):
        return request.param

    @allure.story("Telnet")
    @allure.title("登录成功")
    @pytest.mark.parametrize('login', [handle_yaml.get_yaml_data()['Login']], indirect=True)
    def test_login_pass(self, login):
        lb.logger.info(f"{__name__, sys._getframe().f_code.co_name}>>>>>登录信息:{login}")
        lb.logger.info(f"解包后的账号 和密码 ：{login['username'], login['password']}")
        re = self.tl.login(login['username'], login['password'])
        lb.logger.info(f"运行结果：{re}")
        assert login['expect'] in re

    def teardown_class(self):
        self.tl.exit()


if __name__ == '__main__':
    pytest.main()
