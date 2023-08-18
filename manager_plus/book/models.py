from django.db import models

# Create your models here.

class BookInfo(models.Model):
    book_name = models.CharField(max_length=10)

    def __str__(self):
        return self.book_name

class PeopleInfo(models.Model):
    people_name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.people_name + '——' + self.book.book_name