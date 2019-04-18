# Models 模型   
### ORM （ObjectRelationMap）
- 把面向对象思想转换成关系数据库思想.操作上把类对应表格
- 类中的属性对应表中的字段
- 在应用中的models.py文件中定义class
- 所有需要使用ORM的class都必须是 models.Model 的子类
- class中的所有属性对应表格中的字段
- 字段的类型都必须使用 modles.xxx 不能使用python中的类型
- 在django种，Models负责跟数据库交互

### django链接数据库
- 自带默认数据库Sqllite3
    - 关系型数据库
    - 轻量级
- 建议开发用sqlite3， 部署用mysql之类数据库
    - 切换数据库在settings中进行设置 

>django 连接 mysql
```
DATABASES = [
    'default' = {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : '数据库名',
        'PASSWORD': '数据库密码',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        }]

- 需要在项目文件下的__init__文件中导入pymysql包,在主项目的__init__文件中
import pymysql
pymysql.install_as_MySQLdb()
```
                
# models类的使用
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
- 所有的类型都是以Field()结尾   

## 数据库的迁移
1. 在命令行中,生成数据迁移的语句(生成sql语句)
`python3 manage.py makemigrations`
            
2. 在命令行中,输入数据迁移的指令
    ```sh
    python3 manage.py migrate
    ```

    > 如果迁移中出现没有变化或者报错,可以尝试强制迁移
    
    ```sh
    # 强制迁移命令
    python3 manage.py makemigrations 应用名
    python3 manage.py migrate 应用名
    ```
3. 对于默认数据库， 为了避免出现混乱，如果数据库中没有数据，每次迁移前可以把系统自带的sqlite3数据库删除
    
    
# 查看数据库中的数据

1. 启动命令行 : 
    ```sh
    python3 manage.py shell
    ```
    >注意点: 对orm的操作分为静态函数和非静态函数两种。静态是指在内存中只有一份内容存在,调用的时候使用 类名. 的方式。如果修改了那么所有使用的人都会受影响。

2. 在命令行中导入对应的映射类：
    ```python
    from 应用.models import 类名
    from teacher.models import Teacher
    ```

3. 使用objects属性操作数据库。objects是模型中实际和数据库进行交互的 Manager 类的实例化对象。

4. 查询命令：
	- `类名.objects.all()` 查询数据库表中的所有内容. 返回的结果是一个QuerySet类型,实际上是类列表中装这个一个一个数据对象.
	- `类名.objects.filter(条件)`
    ```python
    from 应用名.models import 类名
    from myapp.models import Student

    #查询Student表中的所有数据,得到的是一个QuerySet类型
    Student.objects.all()

    #如果要取出所有QuerySet类型中的所有数据对象,需要遍历取出所有的对象,再用对象.属性来查看值

    s = Student.object.all()
    for each in s:
	    print(each.name , each.age , each.address , each.phone)

    # 如果要进行过滤筛选,使用filter()方法
    Student.objects.filter(age=18)
    ```
# 添加数据
1. `python3 manage.py shell` # 命令行中添加数据
2. `对象 = 类()`   # 使用类实例化对象
3. `对象.属性 = 值`  # 给对应的对象的属性赋值
4. `对象.save()`  # 必须要执行保存操作,否则数据没有进入数据库

```python
# from 应用名.models import 类名
from myapp.models import Student

# 实例化对象
s = Student()

# 给对象的属性赋值
s.name = '张三'
s.address = '云南昭通'
s.phone = '13377886678'
s.age = 20

# 保存数据
s.save()
```

# 常见查找方法

1. 通用查找格式: `Student.objects.filter(age__gt=值)`
    - gt : 大于
    - gte : 大于等于
    - lt : 小于
    - lte : 小于等于
    - range: 范围
    - year : 年份
    - isnull : 是否为空

2. 查找等于指定值的格式: `Student.objects.filter(age__gt=值)`
3. 特定查找: `Student.objects.filter(age__exact=值)`
    * exact : 精确等于
    * iexact: 不区分大小写
    * contains: 包含
    * startwith: 以..开头
    * endwith: 以…结尾 

# 数据库表关系
- 多表联查：利用多个表联合查找某一项信息或者多项信息

## 1:1 OneToOne
- 建立关系：在模型任意一边即可，使用OneToOneField()
    ```python
    # models.py
    from django.db import models
    
    class School(models.Model):
        school_id = models.IntegerField()
        school_name = models.CharField(max_length=20)

        def __str__(self):
            return self.school_name

    ```
- add:  
    >添加没有关系的一边，直接实例化保存就可以
    ```python
    s = School()
    s.school_id = 2
    s.school_name = "nanjingtulingxueyuan"
    s.save()
    ```

    >添加有关系的一边，使用create方法,或者使用实例化然后save
    ```python
    # 方法1
    m = Manager()
    m.manager_id = 10
    m.manager_name = "dana"
    m.my_school = s
    m.save()
            
    # 方法2
    m = Manager.objects.create(manager_id=20, manager_name="erna", my_school=ss[0])
    ‵‵‵
- query:
    - 有子表查母表： 由子表的属性直接提取信息
    - 由母表查子表：使用双下划线 
    ```python
    s = School.objects.get(manager__manager_name="dana")
    s<School: nanjingtulingxueyuan>
    ```
- change:
    - 单个修改使用save     
    - 批量修改使用update
    - 无论对子表还是对母表的修改
- delete： 直接使用delete还是删除                   
    
## 1:N OneToMany
- 一个表格的一个数据项/对象等，可以有很多个另一个表格的数据项
- 比如：一个学校可以有很多个老师，但一个老师只能在一个学校里上班
- 使用上
    - 使用ForengnKey
    - 在多的那一边，比如上边的例子就是在Teacher的表格里进行定义
        
- Add:
    - 跟一对一方法类似，通过create和new来添加
    - create: 把属性都填满，然后不需要手动保存
    - new: 可以属性或者参数为空，必须用save保存
- Query: 
    - 以学校和老师的例子为准
    - 如果知道老师，查学校，则通过增加的关系属性，直接使用 
    - 例如，查找t1老师是哪个学校的
    - 反查=
        - 有学校，我想查下这个学校所有老师，则系统自动在老师模型名称的小写下直接加下划线set，
                用来表示
            -
## N:N ManyToMany
- 表示任意一个表的数据可以拥有对方表格多项数据，反之亦然
- 比如典型例子就是老师和学生的关系
- 使用上，在任意一方，使用ManyToMany定义，只需要定义一边
- Add:
    - 添加老师，则在student.teachers.add()
- Query:
    - 跟一对多类似，使用_set查询