"""
@File    :   __init__.py.py   
@Modify Time      
@Author       Hongrui 
2024/4/28 16:29      
# >>>TODO 
"""
import xlrd

# file_path = 'autoTelnet_mdu_testcase.xls'
import pytest
import allure
import pandas as pd

@allure.epic('MDU-Test')
@allure.feature('设备信息')
class TestDeviceInfo:

    @pytest.fixture(scope="class")
    def device_info(self):
        # 使用 openpyxl 引擎读取 .xlsx 文件
        file_path = 'autoTelnet_mdu_testcase.xls'
        df = pd.read_excel(file_path, engine='openpyxl')
        return df

    def test_device_info(self, device_info):
        assert not device_info.empty, "设备信息表为空"

    def test_column_names(self, device_info):
        expected_columns = ["Column1", "Column2", "Column3"]
        assert all(column in device_info.columns for column in expected_columns), "列名不匹配"

if __name__ == '__main__':
    pytest.main()
