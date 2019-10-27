from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    message = models.TextField(verbose_name='Сообщение', null=True)
    email = models.EmailField(max_length=30, verbose_name='Email', null=True)

    class Meta:
        verbose_name = 'Сообщение обратной связи'
        verbose_name_plural = 'Сообщения обратной связи'

    def __str__(self):
        return self.name
