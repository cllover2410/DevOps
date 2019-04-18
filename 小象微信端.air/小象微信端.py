# -*- encoding=utf8 -*-
__author__ = "zhangweiwei"



#auto_setup(__file__)

import random
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco # 连接安卓 

"""
poco = AndroidUiautomationPoco()
poco.device.wake() # 唤醒设备
"""
 
#connect_device("android:127.0.0.1:7555") # 选中设备

# 生成手机号
def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # 最后八位数字
    suffix = random.randint(9999999,100000000)
    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)
phone = create_phone()

sleep(3.0)


url = "http://wx.xiaoxiang56.com"

# 登录经纪人
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

driver.get("http://www.xiaoxiang56.com/static/h5/default.html")
driver.find_element_by_xpath("//a[@href='/auth/login']").click()
driver.find_element_by_xpath("//input[@type='text']").send_keys("18610503832")
driver.find_element_by_xpath("//input[@type='password']").send_keys("111111")

#text(123456)
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div[2]/form/div[4]/div/button/span").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/aside/ul/li/ul/li[3]").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div[2]/div/div[2]/div/div/button").click()
driver.find_element_by_xpath("//textarea[@placeholder='详细地址']").send_keys("123456")
driver.find_element_by_xpath("//input[@placeholder='请输入姓名']").send_keys("地址")
driver.find_element_by_xpath("//input[@placeholder='请输入手机号']").send_keys(phone)

touch(Template(r"tpl1555574504249.png", record_pos=(3.395, 1.81), resolution=(381, 723)))
touch(Template(r"tpl1555574508162.png", record_pos=(1.954, 1.377), resolution=(381, 723)))





















