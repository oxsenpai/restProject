from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
class Firm(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Производитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name = 'products',
                                 on_delete = models.CASCADE,
                                 verbose_name = 'Категория')
    firm = models.ForeignKey(Firm,
                             related_name= 'products',
                             on_delete = models.CASCADE,
                             verbose_name= 'Производитель',
                             null = True)
    name = models.CharField(max_length = 150, verbose_name = 'Наименование')
    description = models.TextField(blank = True, null = True, verbose_name = 'Описание')
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Цена')
    available = models.BooleanField(default = True, verbose_name = 'Наличие')
    created = models.DateTimeField(default = datetime.datetime.today, verbose_name = 'Дата добавления')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    country = models.CharField(max_length=2)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    order_notes = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return f'Заказ №{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
    




