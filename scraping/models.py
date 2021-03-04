from random import randint

from django.db import models
from scraping.utils import from_cyrillic_to_eng

class PestProducts(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название продукта', unique=True, default='None')
    group = models.CharField(max_length=50, verbose_name='Группа', default='None')
    brief = models.TextField(verbose_name='Описание', default='None')
    preparation_form = models.CharField(max_length=100, verbose_name='Препаративная форма', default='None')
    intermediate = models.CharField(max_length=100, verbose_name='Действующее вещество', default='None')
    formulation = models.CharField(max_length=50, verbose_name='Формуляция', default='None')
    him_class = models.CharField(max_length=100, verbose_name='Химический класс', default='None')
    how_to_inside = models.CharField(max_length=100, verbose_name='Способ проникновения', default='None')
    how_to_work = models.CharField(max_length=100, verbose_name='Характер действия', default='None')
    danger_people = models.CharField(max_length=50, verbose_name='Класс опасности для человека', default='None')
    danger_oss = models.CharField(max_length=50, verbose_name='Класс опасности для пчел', default='None')
    reg_number = models.CharField(max_length=50, verbose_name='Регистрационный номер', default='None')
    reg_false = models.CharField(max_length=50, verbose_name='Дата окончания срока регистрации', default='None')
    registrant = models.CharField(max_length=100, verbose_name='Регистрант', default='None')
    manufacturer = models.CharField(max_length=100, verbose_name='Производитель', default='None')
    what_prod = models.CharField(max_length=100, verbose_name='Производство', default='None')
    packing = models.TextField(verbose_name='Упаковка', default='None')
    storage = models.CharField(max_length=50, verbose_name='Срок хранения', default='None')
    generics = models.TextField(verbose_name='Аналоги', default='None')
    price_china = models.CharField(max_length=100, verbose_name='Цена в Китае', default='0')
    price_india = models.CharField(max_length=100, verbose_name='Цена в Индии', default='0')
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Пестициды'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.title))
        super().save(*args, **kwargs)


class ReglamentPest(models.Model):

    title = models.ForeignKey(PestProducts, on_delete=models.CASCADE, verbose_name='Название продукта')
    norm_for_use = models.CharField(max_length=50, verbose_name='Норма расхода', default='None')
    crop = models.TextField(verbose_name='Обрабатываемая культура', default='None')
    pest = models.TextField(verbose_name='Вредитель', default='None')
    using = models.TextField(verbose_name='Способ применения', default='None')
    using_time = models.CharField(max_length=50, verbose_name='Кратность обработок', default='None')
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Нормы расхода пестицидов'

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.title)+str(randint(1, 30)))
        super().save(*args, **kwargs)
