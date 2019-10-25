from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('products:category', kwargs={'pk':self.pk})


class Product(models.Model):
    rooms = models.PositiveIntegerField(verbose_name='Количество комнат')
    square = models.FloatField(verbose_name='Площадь')
    address = models.TextField(verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена')
    owner = models.CharField(max_length=200, verbose_name='Владелец')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.EmailField(max_length=30, verbose_name='Email', blank=True, null=True)
    image = models.ImageField(upload_to='products/img', height_field=None, width_field=None, max_length=100, verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, models.PROTECT, verbose_name='Категория', related_name="products")

    class Meta():
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('products:product', kwargs={'pk':self.pk})