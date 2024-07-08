"""
@File    :   handle_yaml.py   
@Modify Time      
@Author       hongrui

# >>>TODO 读取yaml工具类
"""

import yaml
from utils.handle_path import yaml_path_case


def get_yaml_data(dir = yaml_path_case):
    """
    :param filedir: yaml文件的路口
    :return: 返回yaml的数据
    """

    with open(dir, 'r', encoding='UTF-8') as fs:
        return yaml.safe_load(fs)


if __name__ == '__main__':
    # print(get_yaml_data(dir=yaml_path_conf)['serial'])  # <class 'dict'>
    print(get_yaml_data()['Login'])  # <class 'dict'>
    print(get_yaml_data()['Shell'])  # <class 'dict'>
