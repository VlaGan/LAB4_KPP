from django.db import models


class Task(models.Model):
    title = models.CharField('Nickname', max_length=50)
    comment = models.TextField('Comment')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
