'''
@Time    : 2024/5/13 10:18
@Author  : wujie
@Site    : 
@File    : test_deviceInfo.py
@Software: PyCharm 
@Comment : 测试通过 产测接口协议（发送udp）查询设备信息
        SN、MAC、SOFRVersion、HARDVersion、LED、PON、LAN
'''
import json
import pytest
from commcon import log_Base as lb
from commcon import Protocol_Base
from utils import handle_yaml, handle_path, handle_excel


class TestDeviceInfo:

    def setup_class(self):
        # 获取设备串口、telnet连接信息
        self.link_info = handle_yaml.get_yaml_data(handle_path.yaml_path_conf)
        lb.logger.info(f"议连接信息:{self.link_info}")
        self.pb = Protocol_Base.MultiProtocolCommunicator(serial_port=self.link_info[1]['serial']['ser_port'],
                                                          baudRate=self.link_info[1]['serial']['ser_baudRate'],
                                                          telnet_ip=self.link_info[0]['telnet']['tn_ip'],
                                                          telnet_port=self.link_info[0]['telnet']['tn_prot'],
                                                          udp_ip=self.link_info[2]['product_test']['pt_ip'],
                                                          udp_port=self.link_info[2]['product_test']['pt_port'])
        # 上电-发送串口指令 上电参数：serial_open_command
        message = [mes for mes in self.link_info[3]['serial_open_command'].values()]
        lb.logger.info(f"发送的指令，上电参数：{message}")
        self.pb.send_serial(message_list=message)
        # 发起socket连接【udp 产测】
        # 发起telnet连接，登录，切换su用户
        self.pb.link()
        self.pb.login(username=self.link_info[0]['telnet']['tn_username'],
                      password=self.link_info[0]['telnet']['tn_password'])
        self.pb.shell(command=self.link_info[0]['telnet']['tn_root_username'])
        self.pb.shell(command=self.link_info[0]['telnet']['tn_root_password'])
        # 启动产测进程
        self.pb.shell(command='cd /bin/')
        self.pb.shell(command='cncr_product_test')

    @pytest.mark.timeout(60)
    @pytest.mark.parametrize('case_list_command', handle_excel.getFiltrateData('product_test'))
    def test_device_info(self, case_list_command):
        lb.logger.info(f" 测试用例集：{case_list_command}")
        lb.logger.info(
            f" 测试用例名称：{case_list_command['case_name']},测试用例类型：{case_list_command['case_type']}, 测试用例步骤：{type(case_list_command['case_step'])},测试用例步骤：{case_list_command['case_step']} ")
        device_expect = case_list_command['expect_result'].replace('\n', '')
        lb.logger.info(f"用例期望结果：{type(device_expect)}， {device_expect} ")

        re_udp = self.pb.send_udp(case_list_command['case_step']).replace('\x00', '')
        lb.logger.info(
            f"用例执行结果，收到消息 :  {type(re_udp)} {re_udp}, code: {json.loads(re_udp)['result_code']}, msg: {json.loads(re_udp)['result_msg']}")
        assert json.loads(re_udp)['result_code'] == 'OK'
        assert json.loads(re_udp)['result_msg'] == 'handle cmd success'
        # if 'data' in re_udp:
        #     if 'interface_status' in re_udp:
        #         re_udp.replace('\\', '')  # 获取端口link状态 会返回 / 被转义成\/
        #     else:
        #         assert json.loads(re_udp)['data']['data1'] == json.loads(device_expect)['data']['data1']

    def teardown_class(self):
        message = [mes for mes in self.link_info[4]['serial_close_command'].values()]
        lb.logger.info(f"发送的指令，下电参数：{message}")
        self.pb.send_serial(message_list=message)
        lb.logger.info("我断后了~~")
        self.pb.close()


if __name__ == '__main__':
    pytest.main('-vs')
