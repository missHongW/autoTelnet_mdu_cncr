"""
@File    :   log_Base.py   
@Modify Time      
@Author       Hongrui

# >>>TODO 封装日志
"""

import logging
import os
from utils import handle_path

# 创建日志收集器
logger = logging.getLogger('CNCR-MDU产品自动化测试日志')

# 设置日志的级别  debug  info  warning  error  critical
logger.setLevel(logging.INFO)

# 设置输出的渠道
handle = logging.StreamHandler()  # 输出到控制台
# 定义文件路径
logfile = os.path.join(handle_path.project_path, 'outfile', 'logfile.log')
handle = logging.FileHandler(filename=logfile, mode='w', encoding='utf-8')  # 输出到文件中
# 日志的格式 ：时间、日志级别[日志名称][日志所在的文件名称:日志所在函数名称:行号][输入自定义的内容]
fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s %(funcName)s:%(lineno)d] - %(message)s'
f = logging.Formatter(fmt)

# 日志格式和渠道绑定
handle.setFormatter(f)

# 日志收集器和渠道绑定
logger.addHandler(handle)


if __name__ == '__main__':
    name = 'jack'
    age = 12
    logger.info(f'我是 {name}，今年 {age} info级别的日志')
    logger.debug('我是debug级别的日志')
    logger.error('我是error级别的日志')
