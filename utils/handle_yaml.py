"""
@File    :   handle_yaml.py   
@Modify Time      
@Author       wujie 
2024/4/28 17:19      
# >>>TODO 读取yaml工具类
"""

import yaml
from utils import handle_path
from handle_path import yaml_path_case


def get_yaml_data(dir=yaml_path_case):
    """
    :param filedir: yaml文件的路口
    :return: 返回yaml的数据
    """

    with open(dir, 'r', encoding='UTF-8') as fs:
        return yaml.safe_load(fs)


if __name__ == '__main__':

    print(get_yaml_data()['Link'])  # <class 'dict'>
    print(get_yaml_data()['Login'])  # <class 'dict'>
    print(get_yaml_data()['shell'])  # <class 'dict'>
