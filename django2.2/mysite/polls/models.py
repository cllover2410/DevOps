
# Create your models here.
from django.db import models

'''
代码非常直白。每个模型被表示为 django.db.models.Model 类的子类。
每个模型有一些类变量，它们都表示模型里的一个数据库字段。

'''
class Question(models.Model):

    '''
    每个字段都是 Field 类的实例 
    - 比如，字符字段被表示为 CharField ，日期时间字段被表示为 DateTimeField 。
    这将告诉 Django 每个字段要处理的数据类型。
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)




