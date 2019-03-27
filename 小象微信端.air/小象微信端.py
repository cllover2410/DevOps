# -*- encoding=utf8 -*-
__author__ = "zhangweiwei"

from airtest.core.api import *

auto_setup(__file__)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome

import random
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
# 生成手机号
phone = create_phone()


url = "http://192.168.4.176:8080/"


企业货主 = WebChrome()
企业货主.implicitly_wait(20)
企业货主.get(url)

'''
个人货主 = WebChrome()
个人货主.implicitly_wait(20)
个人货主.get(url)
'''

经纪人 = WebChrome()
经纪人.implicitly_wait(20)
经纪人.get(url)

司机 = WebChrome()
司机.implicitly_wait(20)
司机.get(url)

