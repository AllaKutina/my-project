from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    rooms = models.PositiveIntegerField(verbose_name='Количество комнат')
    square = models.FloatField(verbose_name='Площадь')
    address = models.TextField(verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена')
    owner = models.CharField(max_length=200, verbose_name='Владелец')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.EmailField(max_length=30, verbose_name='Email', blank=True, null=True)
    category = models.ForeignKey(Category, models.PROTECT, verbose_name='Категория')

    class Meta():
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'