from django.db import models


class Message(models.Model):
    # 留言者姓名
    name = models.CharField(max_length=50)

    # 留言内容
    content = models.TextField()

    # 留言创建时间
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
