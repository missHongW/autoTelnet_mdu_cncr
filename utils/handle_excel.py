# -*- coding: utf-8 -*-
"""
@File    :   handle_excel.py
@Modify Time
@Author  : HongRui

# >>>TODO
读取Excel中数据
"""

import json
import pandas as pd
from utils.handle_path import case_path
from commcon import log_Base as lb

testData_path = r"%s" % (case_path)
print("测试用例位置>>>", testData_path)


try:
    excel_data = pd.read_excel(testData_path, engine='openpyxl')
except ValueError as e:
    # 如果 openpyxl 引擎失败，尝试使用 xlrd 引擎
    if 'Excel xlsx file; not supported' in str(e):
        excel_data = pd.read_excel(testData_path, engine='xlrd')
    else:
        raise e

# 获取Excel文件中的第一个表格
excel_sheet_first = excel_data


def get_excel_data(file_path, sheet_name):
    '''
    :param file_path: 文件的路径
    :param sheet_name: 具体操作的sheet名称
    :return: [(),()]   列表套元组
    '''
    print("get_excel_data_file_path", file_path)
    # 尝试使用 openpyxl 引擎读取文件
    try:
        work_book = pd.ExcelFile(file_path, engine='openpyxl')
    except ValueError as e:

        if 'Excel xlsx file; not supported' in str(e):
            work_book = pd.ExcelFile(file_path, engine='xlrd')
        else:
            raise e

    # 2- 指定对于的列表
    print(work_book.sheet_names())  # 查看文件的表名称

# 获取指定行的数据
def getExcelRowDatas(rowx, start_colx=0, end_colx=None):
    '''
    :param rowx: 获取第x行的数据, 从0开始
    :param start_colx:  开始第x列 不传则默认是0第一列开始
    :param end_colx:  结束第x列，不传则默认是全部
    :return: 列表类型的数据<class 'list'>
    '''
    # 获取excel表格中第x行的数据
    excel_row_datas = excel_sheet_first.iloc[rowx, start_colx:end_colx].tolist()
    return excel_row_datas

# 获取指定列的数据
def getExcelColDatas(colx, start_rowx=1, end_rowx=None):
    '''
    :param colx: 获取第x列的数据
    :param start_rowx: 开始第x行 不传则默认是1
    :param end_rowx: 结束第x行 不传则默认是全部
    :return: 列表类型的数据 <class 'list'>
    '''
    excel_col_datas = excel_sheet_first.iloc[start_rowx:end_rowx, colx].tolist()
    return excel_col_datas


def getExcelCellData(rowx, colx):
    '''
    获取任意单元格的数据
    :param rowx: 行
    :param colx: 列
    :return: 字符串类型返回单元格内容  <class 'str'>
    '''
    excel_cell_datas = excel_sheet_first.iloc[rowx, colx]
    return excel_cell_datas


def getFiltrateData(type):
    '''
    通过参数筛选到指定的数据
    :param type: 测试用例文件中的用例类型
    :return: 筛选后的数据
    '''
    # 初始化一个列表存放筛选后的数据
    resulte_filtrate = []

    print(len(excel_sheet_first), "excel_sheet_first.nrows")
    for row_num in range(0, len(excel_sheet_first)):
        # 用例名称
        case_name = getExcelCellData(row_num, 2)
        print("row_num, case_name", row_num, case_name)
        # 用例类型
        case_type = getExcelCellData(row_num, 3)
        print("协议类型："+case_type)
        # 用例步骤
        case_step = getExcelCellData(row_num, 5)
        # 期望结果
        expect_result = getExcelCellData(row_num, 6)
        # 符合类型的数据存放在列表中并返回
        if case_type == type:
            resulte_filtrate.append({'case_name': case_name, 'case_type': case_type, 'case_step': case_step,
                                     'expect_result': expect_result})

            resulte_filtrate_json = json.dumps(resulte_filtrate, ensure_ascii=False, indent=2)
            lb.logger.info(f"获取筛选后的用例数据：{resulte_filtrate_json}")

    return resulte_filtrate


if __name__ == '__main__':
    print(getFiltrateData('product_test'))
