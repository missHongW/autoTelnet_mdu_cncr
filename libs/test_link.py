"""
@File    :   test_link.py   
@Modify Time      
@Author       wujie 
2024/4/29 15:57      
# >>>TODO 连接Telnet
"""

import pytest
from utils import handle_yaml
from commcon import telnet_Base as tb



class TestLink:

    @pytest.fixture()
    def ip(self, request):
        self.tl = tb.TelnetLib()
        return request.param

    @pytest.mark.parametrize('ip', [handle_yaml.get_yaml_data()['Link']], indirect=True)
    def test_link_pass(self, ip):
        print(ip.get('ip'))
        print(ip.get('expect'))
        re = self.tl.link(ip.get('ip'))
        assert ip.get('expect') in re



if __name__ == '__main__':
    pytest.main()