from django.db import models


# Create your models here.

class ShowTable(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    quantity = models.PositiveIntegerField(default=0)
    distance_entity = models.PositiveIntegerField(default=0)
    date_entity = models.DateTimeField()

    class Meta:
        app_label = 'web_table'
        db_table = 'showtable'
        ordering = ['-id']
        managed = False


class ShowTableFilter(models.Model):
    NAME = 'Название'
    QUANTITY = 'Количество'
    DISTANCE = 'Расстояние'
    EQUALS = 'Равно'
    CONTAINS = 'Содержит'
    MORE = 'Больше'
    LESS = 'Меньше'

    COLUMN_CHOICES = (
        (NAME, 'Название'),
        (QUANTITY, 'Количество'),
        (DISTANCE, 'Расстояние'),
    )
    CONDITION_CHOICES = (
        (EQUALS, 'Равно'),
        (CONTAINS, 'Содержит'),
        (MORE, 'Больше'),
        (LESS, 'Меньше'),
    )
    column = models.CharField(
        verbose_name='столбец',
        max_length=10,
        choices=COLUMN_CHOICES,
        blank=True,
    )
    condition = models.CharField(
        verbose_name='условие',
        max_length=10,
        choices=CONDITION_CHOICES,
        blank=True,
    )
    value_input = models.CharField(
        verbose_name='значение',
        max_length=10,
        blank=True,
    )
