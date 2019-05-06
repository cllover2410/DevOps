from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100) # CharField -- 字串欄位，適合像 title、location 這種有長度限制的字串。
    content = models.TextField(blank =True) # TextField -- 合放大量文字的欄位
    photo =  models.URLField(blank = True) # URLField -- URL 設計的欄位
    location = models.CharField(max_length = 100) 
    created_at = models.DateTimeField(auto_now_add = True) # DateTimeField -- 日期與時間的欄位，使用時會轉成 Python datetime 型別。
    
    def __str__(self):
        return self.title