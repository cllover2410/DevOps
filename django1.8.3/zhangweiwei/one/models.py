
'''
- 定义和数据库表映射的类
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是 models.Model 的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用 modles.xxx 不能使用python中的类型
- 字段常用参数
    1. max_length : 规定数值的最大长度
    2. blank : 是否允许字段为空,默认不允许
    3. null : 在DB中控制是否保存为null, 默认为false
    4. default : 默认值
    5. unique : 唯一
    6. verbose_name : 假名

- 数据库的迁移
    1. 在命令行中,生成数据迁移的语句(生成sql语句)
            ```
            # 准备迁移
            python3 manage.py makemigrations
            ```
    2. 在命令行中,输入数据迁移的指令
            ```
            python3 manage.py migrate
            ```
            ps : 如果迁移中出现没有变化或者报错,可以尝试强制迁移
            ```
            # 强制迁移命令
            python3 manage.py makemigrations 应用名
            python3 manage.py migrate 应用名
            ```
    3. 对于默认数据库， 为了避免出现混乱，如果数据库中没有数据，每次迁移前可以把系统自带的sqlite3数据库删除
        - 删除migrations
        - 删除sql3
'''


from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=20)