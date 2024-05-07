# This is a sample Python script.
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pytest


if __name__ == '__main__':
    # # 1. 使用pytest生成测试报告时需要传递一个列表
    # json_dir_path = 'outfile/result'
    # args_list = ['-s', '-v', '--alluredir', json_dir_path, '--clean-alluredir']
    # pytest.main(args_list)
    #
    # # 2. 使用allure命令生成测试报告 ：allure generate 数据路径文件 -o html路径文件 -c
    # # cmd = 'allure generate {} -o report -c'.format(json_dir_path)
    # # print(cmd)
    # # os.system('allure generate result -o outfile/report -c')
    # os.system('allure serve outfile/result')

    args = ['-vs',
            '--report=MDU产品自动化测试报告.html',
            '--title=MDU产品自动化测试报告',
            '--tester=自动化机器',
            '--desc=这是MDU产品自动化测试报告，包含测试用例数、执行花费时间、执行日期、执行用例结果',
            '--template=2']
    pytest.main(args)