

### 常用字段类型

### 数值类型
#### 1. `AutoField` 
- 自增主键，Django Model默认提供，可以被重写
- `int(11)`
```python
id = models.AutoField(primary_key = True)
```

#### 2. `BoolleanField`
- 布尔类型字段，一般用于记录状态标记。
- `tinyint(1)`

#### 3. `DecimalField decimal`
- 


#### 4. `IntegerField`

#### 

---
## 字符类型
这些字符都是用来存储字符数据的，



### 日期类型
分别对应Mysql的date、datetime、time
- `DateField` 
- `DateTimeFile`
- `TimeField`

### 4. 关系类型
#### `ForeignKey`
#### `OneToOneField`
- 外键和一对一其实是一种，只是一对一在外键的字段上加了`unique`。而多对多会创建一个中间表来进行多对多的关联。

#### `ManyToManyField`
---
