"""
@File    :   test_link.py   
@Modify Time      
@Author       HongRui
@Description    :
# >>>TODO 连接Telnet
# >>>TODO 使用pytest框架进行测试
# >>>TODO 使用allure框架进行测试结果的管理和展示
# >>>TODO 使用yaml文件进行配置
# >>>TODO 使用log库进行日志记录
# >>>TODO 使用工厂模式进行telnet链接的创建
# >>>TODO 使用装饰器进行测试用例的标记
# >>>TODO 使用上下文管理器进行telnet链接的关闭
"""

import pytest
import allure
import sys
from utils import handle_yaml
from commcon import Telnet_Link as tb
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
        print(f"解包后的账号 和密码 ：{login['username'], login['password']}")
        re = self.tl.login(login['username'], login['password'])
        lb.logger.info(f"运行结果：{re}")
        print(f"运行结果：{re}")

        assert login['expect'] in re

    def teardown_class(self):
        self.tl.exit()


if __name__ == '__main__':
    pytest.main()
