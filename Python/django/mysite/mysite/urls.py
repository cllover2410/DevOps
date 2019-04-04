"""mysite URL Configuration (mysite url配置)

The `urlpatterns` list routes URLs to views. For more information please see (“urlpatterns”列表将URL路由到视图。有关更多信息，请参阅):
    https://docs.djangoproject.com/en/1.8/topics/http/urls/

Examples:
Function views（功能视图）
    1. Add an import (添加导入):  from my_app import views
    2. Add a URL to urlpatterns (向urlpatterns添加URL):  url(r'^$', views.home, name='home')

Class-based views (基于类的视图)
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')

Including another URLconf (包括一个URLconf)
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'test\Python\django\mysite\mysite'))
	print(os.getcwd())
except:
	pass

#%%
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^withparam/ \(?P<year>[0-9]{4})/(?P<month>[0-1][0-9])', "learn.views.withparam"), 
    url(r"^$", "learn.views.index", name="one") # 反向解析
]


#%% [markdown]
# # 路由系统
# - 按照具体的请求url，导入到相应的业务处理模块的一个功能模块
# - django的信息控制中枢
# - 本质上是接受的URL和相应的处理模块的一个映射
# - 在接受URL请求的匹配上使用RE
# - 需要关注的两点:
#   - 接受的URL是什么，及如何用RE对传入URL进行匹配
#   - 已知URL匹配到哪个处理模块

#%% [markdown]
# ## 1. Url匹配规则
# - 从上往下一个一个对比
# - url格式是分级格式，则按照级别一级一级往下对比，主要对应url包含子url的情况
# - 子url一旦被调用，则不会返回到主url
#   - '/one/two/three/'
# - 正则以r开头，表示不需要转义，注意尖号^和美元符号$
#   - '/one/two/three' 匹配 r'^one/'
#   - '/oo/one/two/three' 不配对 r'^one/'
#   - '/one/two/three/' 配对 r'three/$'
#   - '/oo/one/two/three/oo/' 不配对 r'three/$'
#   - 开头不需要有反斜杠
#   - 如果从上往下都没有找到合适的匹配内容，则报错

#%% [markdown]
# ## 2. 基本映射
#   - 把某一个符合RE的URL映射带事物处理函数中去

#%% [markdown]
# ## 3. URL中带参数
#   - 从事件处理代码中需要由URL传入参数，形如 /myurl/param中的param
#   - 参数通常是字符串形式了，如果需要整数等形式需要自行转换 
#   - 通常形式如下：
#        - /search/page/432 中的432需要经常性变化，所以写成参数
#        - ?P 

#%% [markdown]
# ## 4. URL在app中处理
# - 如果所以应用URL都集中在项目urls.py中，可能导致文件的臃肿
# - 可以把urls具体功能逐渐分散到每个app中
#   - 从 django.conf.urls 导入 include 
#       - from django.conf.urls import include
#           - 注意此时RE部分的写法
#           - 添加include导入
#    - 使用方法
#           - 确保include被导入
#           - 写主路由的开头url
#           - 写子路由
#           - 编写views函数
#    - 同样可以使用参数

#%% [markdown]
# ## 5. URL中的嵌套参数
# - 捕获某个参数的一部分
#   - 例如URL /index/page-3，需要捕获数字3作为参数
#        '''
#            url(r'index_1(page-(\d+)/)?$', sv.myindex_1), # 不友好
#            url(r'idnex_2(?:page-(?P<page_number>\d+)/)', sv.myindex_2)#友好
#        '''
#        - 上述列子会得到两个参数，但?:表示忽略此参数
#

#%% [markdown]
# ## 6. 传递额外参数
# - 参数不仅仅来自URL，还可能是我们自己定义的内容
# '''
#            url(r'extrem/$, sv.extremParam', {'name': "zhangweiwei"}),
# '''
# - 附加参数同样适用于include语句，此时对include内所有的都添加
#
# ## 7. URL的反向解析
#    - 防止硬编码
#        - 本质是对每个URL进行命名
#        - 以后在编码代码中使用URL的值，原则上都应该使用反向解析
#    - url 里面设置name属性
# - URL在app中处理
# - url(r'^donormalmap/' do_normalmap), # 基本映射

# 带参数的映射 

# 视图函数名称只有名称，无括号和参数
# 圆括号表示的是一个参数，里面的内容作为参数传递给被调用的函数
# 参数名称以问号加大写P开头，尖括号里面就是参数的名字
# 尖括号后表示正则，[0-9]表示内容仅能是有0-9的数字构成
# 后面大括号表示出现的次数，此处4表示只能出现4个0-9的数字
# 反向解析

