"""
@File    :   handle_yaml.py   
@Modify Time      
@Author       wujie 
2024/4/28 17:19      
# >>>TODO 读取yaml工具类
"""

import yaml
from utils import handle_path


def get_yaml_data(dir):
    """
    :param filedir: yaml文件的路口
    :return: 返回yaml的数据
    """

    with open(dir, 'r', encoding='UTF-8') as fs:
        return yaml.safe_load(fs)


if __name__ == '__main__':
    yamldir = handle_path.yaml_path
    print(yamldir)
    print(get_yaml_data(yamldir)['Link'])  # <class 'dict'>
    print(get_yaml_data(yamldir)['Login'])  # <class 'dict'>
