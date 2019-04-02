# -*- encoding=utf8 -*-
__author__ = "zhangweiwei"


auto_setup(__file__)


import random
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco()
poco.device.wake()
init_device("Android") 
connect_device("android:127.0.0.1:7555") # 选中设备


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







# 登录司机
home()
poco(text = '#2 QQ浏览器').click()
# poco(name = '搜索或输入网址').click()
# text('http://wx.xiaoxiang56.com')
# poco(name = '智能语音').click()
#poco(name = '请输入手机号').click()
#text(str(18682299065))
#poco(name = '登录').click()
#sleep(10) # 输入验证嘛


# 登录个人货主
home()
poco(text = '#3 QQ浏览器').click()



# 登录经纪人
home()
poco(text = '#1 QQ浏览器').click()
v = (144, 638)
touch(v ,times=2)
touch(Template(r"tpl1554108976745.png", record_pos=(0.003, 0.712), resolution=(576.0, 1024.0)))
