
# 常用字段类型

## 数值类型
#### 1. `AutoField int(11)` 
- 自增主键，Django Model默认提供，可以被重写
```python
id = models.AutoField(primary_key = True)
```

#### 2. `BoolleanField tinyint(1)`
- 布尔类型字段，一般用于记录状态标记。

#### 3. `DecimalField decimal`
- 开发对数据精度要求较高的业务时考虑使用。

#### 4. `IntegerField int(11)`
- 同 `AutoField`，但是不自增

####  5. `IntergerField`
- 同 `IntergerField`，只包含正整数。

#### 6. `SmallIntegerField smallint`
- 小整数时一般会用到。

---
## 字符类型
这些字符都是用来存储字符数据的，对应到Mysql中有两种类型：`longtext`和`varchar`。除了

#### `CharField varchar`
- 基础的varcahr 类型
#### `URLField`
#### `UUIDField char(32)`
#### `EmailField`
#### `FileField`
#### `TextField longtext`
#### `ImageField`












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
