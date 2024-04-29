"""
@File    :   handle_path.py   
@Modify Time      
@Author       wujie 
2024/4/28 17:20      
# >>>TODO 读取文件路径工具类
"""
import os


# 获取当前文件的路径
current_path = os.path.abspath(__file__)
# print(current_path)
# 获取当前工程的路径
project_path = os.path.dirname(os.path.dirname(current_path))
# print(project_path)

# 获取yaml文件的路径
yaml_path_conf = os.path.join(project_path, 'configs', 'config.yaml')
yaml_path_case = os.path.join(project_path, 'data', 'autoTelnet_mdu_testcase.yaml')
# print(yaml_path)

# 获取用例文件的路径
case_path = os.path.join(project_path, 'data', 'autoTelnet_mdu_testcase.xls')


# case_data = os.path.join(project_path, 'TestCase', 'case_data.yaml')
print(yaml_path_case)
