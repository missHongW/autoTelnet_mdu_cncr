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
import logging


@allure.epic('MDU-Test')
@allure.feature('连接Telnet')
class TestLink:

    def setup_class(self):
        self.tl = tb.TelnetLib()

    @pytest.fixture()
    def ip(self, request):
        return request.param

    @allure.story("Telnet")
    @allure.title("启用连接")
    @pytest.mark.parametrize('ip', [handle_yaml.get_yaml_data()['Link']], indirect=True)
    def test_link_pass(self, ip):
        lb.logger.info(f"{__name__, sys._getframe().f_code.co_name}>>>>>ip连接信息:{ip}")
        lb.logger.info(f"{__name__, sys._getframe().f_code.co_name}>>>>>连接的ip地址:{ip.get('ip')}")
        lb.logger.info(f"{__name__, sys._getframe().f_code.co_name}>>>>>预期结果值:{ip.get('expect')}")
        re = self.tl.link(ip.get('ip'))
        lb.logger.info(f"运行结果：{re}")
        assert ip.get('expect') in re

    def teardown_class(self):
        self.tl.exit()


if __name__ == '__main__':
    pytest.main()
