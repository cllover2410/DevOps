# admin
## 1. 创建Admin
- settings中填入app
    ```python
    INSTALLED_APPS =[
        'app_name',
    ]
    ```
- 打开urls.py
    ```python
    urlpatterns = [
        url(r'admin/', admin.site.urls),
    ]
    ```
- 创建超级用户
    ```sh
    python manage.py createsuperuser
    ```
- 配置settings文件

## 2. 绑定管理模型

## 3. 设置admin管理类
- 实现方式
    - ModelAdmin
    - 装饰器
- 修改页面显示数量：list_per_page
- 操作选项： actions_on_top/button 
- 控制列表中显示的内容：list_display=[]
- 将方法作为列显示
    - 函数必须返回值
    - 设置short_descraption作为显示内容
    - 排序使用admin_order_field
- 关联对象
    - 使用方法
    
- 右侧过滤器
    
- 搜索框
- 分组显示
