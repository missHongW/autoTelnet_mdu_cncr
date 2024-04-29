"""
@File    :   test_link_case.py
@Modify Time      
@Author       wujie 
2024/4/28 17:52      
# >>>TODO   获取测试用例并发起测试对标
"""
import sys
import pytest, allure
from utils import handle_yaml
from commcon import telnet_Base, log_Base as log



re_yaml = handle_yaml.get_yaml_data()['Link']
print(re_yaml, "re_yaml>>>>>")

class TestLink():
    @pytest.mark.parametrize('ip', re_yaml)
    def test_link_pass(self, ip):
        print(ip['ip'])
        assert ip['ip'] == '192.168.1.1'



if __name__ == "__main__":
    pytest.main()