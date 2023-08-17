from django.db import models

# Create your models here.


'''
1.我们模型类 需要继承自models.Model
2.系统会自动为我们添加一个主键--id
3.字段
    字段名=model.类型（选项）
    字段名数据表字段名
'''
# 准备数据信息
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10)

    # 重写str方法来让admin显示书籍名字
    def __str__(self):
        return self.name

# 人物
class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    


