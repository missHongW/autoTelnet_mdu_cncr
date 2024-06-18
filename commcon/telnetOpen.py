# -*- coding: utf-8 -*-
# @Time    : 2024/6/17 下午2:05
# @Author  : HongRui
# @File    : selenium_login.py
# @Software: PyCharm
# @Comment : 使用Selenium自动化登录后台网站

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class WebLogin:

    def __init__(self):
        # 初始化 WebDriver，假设使用 Chrome 浏览器
        self.driver = webdriver.Edge()

    def login(self, url, username, password):
        # 连接到后台网站
        self.driver.get(url)

        # 找到用户名输入框并清除已有内容，然后输入用户名
        username_input = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        self.driver.execute_script("arguments[0].value = '';", username_input)
        username_input.send_keys(username)

        # 找到密码输入框并清除已有内容，然后输入密码
        password_input = self.driver.find_element(By.XPATH, '//*[@id="logincode"]')
        self.driver.execute_script("arguments[0].value = '';", password_input)
        password_input.send_keys(password)

        # 提交登录表单
        password_input.send_keys(Keys.RETURN)

        # 等待页面加载cx
        time.sleep(2)

        # 检查登录是否成功
        try:
            element = self.driver.find_element_by_xpath('//*[@id="menu_name"]')

            print("登录成功！")
        except NoSuchElementException as e:
            print(f"登录失败！{e}")

    def close(self):
        # 关闭浏览器
        self.driver.quit()


if __name__ == "__main__":
    url = "http://192.168.1.1"
    username = "CMCCAdmin"  # 替换为实际用户名
    password = "aDm8H%MdA"  # 替换为实际密码

    web_login = WebLogin()
    try:
        web_login.login(url, username, password)
    except Exception as e:
        print(f"登录失败: {e}")
    finally:
        web_login.close()
