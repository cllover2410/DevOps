# -*- encoding=utf8 -*-
__author__ = "zhangweiwei"


import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome


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



url = ["http://wx.xiaoxiang56.com", "http://www.xiaoxiang56.com"]

class Pc():
    """
    生成浏览器实例
    """
    def __init__(self):
        self.driver = WebChrome()
        self.driver.implicitly_wait(20)
        self.driver.get(url[1])
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//a[@href='/auth/login']").click()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys("18610503832")
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("111111")
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div[2]/form/div[4]/div/button/span").click()
        self.driver.refresh()
        
        driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div[2]/div/div[2]/div/button/span").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div[2]/div/div[2]/div/button/span").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div[2]/div/div[2]/form/div/div/div[2]/div/div/div/div/input").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/ul/li[2]/span").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div[2]/div/div[2]/form/div/div/div[2]/div[3]/div/div/input").click()
driver.find_element_by_xpath("/html/body/div[4]/div[2]/button/span").click()
driver.find_element_by_xpath("//input[@placeholder='请输入重量']").click()
driver.find_element_by_xpath("//input[@placeholder='请输入价格']").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div[2]/div/div[2]/form/div[5]/div/div/button").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div[2]/div/div[3]/div/div[2]/div[2]/div[3]/table/tbody/tr/td/div/label/span/span").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div[2]/div/div[3]/div/div[3]/span/button/span").click()

        
主账号 = Pc()
