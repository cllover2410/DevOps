# -*- encoding=utf8 -*-
__author__ = "zhangweiwei"


auto_setup(__file__)


import random
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco()
poco.device.wake()
init_device("Android") 
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
touch(Template(r"tpl1554191030281.png", record_pos=(-0.344, -0.449), resolution=(1080, 1920)))
touch(Template(r"tpl1554192183841.png", record_pos=(0.312, 0.282), resolution=(1080, 1920)))
touch()
touch(Template(r"tpl1554174125976.png", rgb=True, target_pos=2, resolution=(1080, 1920)))
# target_pos 点击点
# record_pos 录制时在屏幕中的位置 record_pos=(0.329, -0.478)
# resolution 分辨率

touch(Template(r"tpl1554191113513.png", record_pos=(0.055, -0.544), resolution=(1080, 1920)))
touch(Template(r"tpl1554174125976.png", target_pos=8, record_pos=(0.329, -0.478), resolution=(1080, 1920)))
touch(Template(r"tpl1554191131275.png", record_pos=(0.069, -0.3), resolution=(1080, 1920)))
touch(Template(r"tpl1554191208689.png", record_pos=(-0.378, -0.193), resolution=(1080, 1920)))
touch(Template(r"tpl1554191410601.png", target_pos=6, record_pos=(-0.003, 0.079), resolution=(1080, 1920)))
touch(Template(r"tpl1554191246850.png", record_pos=(-0.381, -0.047), resolution=(1080, 1920)))
touch(Template(r"tpl1554191430025.png", target_pos=6, record_pos=(-0.002, 0.081), resolution=(1080, 1920)))
touch(Template(r"tpl1554191281433.png", record_pos=(-0.332, 0.097), resolution=(1080, 1920)))
touch(Template(r"tpl1554177013126.png", record_pos=(-0.108, 0.051), resolution=(1080, 1920)))
touch(Template(r"tpl1554177022256.png", record_pos=(-0.001, 0.654), resolution=(1080, 1920)))
touch(Template(r"tpl1554177036935.png", record_pos=(-0.001, 0.245), resolution=(1080, 1920)))
touch(Template(r"tpl1554191377041.png", record_pos=(-0.123, 0.23), resolution=(1080, 1920)))
touch(Template(r"tpl1554177050718.png", record_pos=(0.373, 0.231), resolution=(1080, 1920)))
touch(Template(r"tpl1554177057508.png", record_pos=(0.375, 0.679), resolution=(1080.0, 1920.0)))
touch(Template(r"tpl1554177080451.png", record_pos=(-0.307, 0.394), resolution=(1080.0, 1920.0)))
touch(Template(r"tpl1554191480368.png", record_pos=(0.368, 0.521), resolution=(1080, 1920)))
touch(Template(r"tpl1554191534161.png", record_pos=(-0.123, 0.676), resolution=(1080.0, 1920.0)))
touch(Template(r"tpl1554191537117.png", record_pos=(-0.374, 0.698), resolution=(1080.0, 1920.0)))
touch(Template(r"tpl1554191542670.png", record_pos=(-0.123, 0.676), resolution=(1080.0, 1920.0)))
touch(Template(r"tpl1554191546441.png", record_pos=(-0.121, 0.237), resolution=(1080.0, 1920.0)))

touch(Template(r"tpl1554177092110.png", record_pos=(0.373, 0.679), resolution=(1080.0, 1920.0)))
touch(Template(r"tpl1554181304460.png", record_pos=(-0.259, 0.281), resolution=(1080.0, 1920.0)))
touch(Template(r"tpl1554181308942.png", record_pos=(-0.159, -0.417), resolution=(1080.0, 1920.0)))
touch(Template(r"tpl1554181318237.png", record_pos=(0.313, 0.683), resolution=(1080.0, 1920.0)))
touch(Template(r"tpl1554181324614.png", record_pos=(0.001, 0.676), resolution=(1080.0, 1920.0)))
touch(Template(r"tpl1554181330832.png", record_pos=(0.003, 0.679), resolution=(1080.0, 1920.0)))














