"""
@File    :   test.py   
@Modify Time      
@Author       wujie 
2024/4/28 14:04      
# >>>TODO 
"""

import paramiko

# 连接信息
ssh_host = '192.168.20.71'
ssh_username = 'zet'
ssh_password = 'Admin@123'

# 创建ssh客户端
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    # 连接远程主机
    ssh_client.connect(ssh_host, username=ssh_username, password=ssh_password)

    # 执行命令
    stdin, stdout, stderr = ssh_client.exec_command('iperf3  -c 192.168.20.30')

    # 获取命令结果
    ssh_out = stdout.read().decode('utf-8')
    print(ssh_out)
except Exception as e:
    print(e)
    print(stderr.read().decode('utf-8'))
finally:
    ssh_client.close()