from django.db import models
import datetime


class Post(models.Model):

        group_id=models.CharField(verbose_name='Id канала для постинга',max_length=255, )
        text = models.CharField(verbose_name='Текст поста',max_length=255, default=0)
        vars = (
            ('off', '0'),
            ('on', '1')
            )
        photo = models.CharField(verbose_name='путь к фото',max_length=255, default=0,choices=vars)
        file = models.CharField(verbose_name='путь к файлу',max_length=255,default=0,choices=vars )
        video = models.CharField(verbose_name='путь к видео',max_length=255,default=0,choices=vars )
        

        reactions=models.CharField(verbose_name='добавить реации',max_length=255,default=0,choices=vars )
        
        posting_date = models.DateTimeField(
            'Дата постинга', default=datetime.datetime.now() + datetime.timedelta(days=1, hours=2))

        def __str__(self):
            return self.group_id

