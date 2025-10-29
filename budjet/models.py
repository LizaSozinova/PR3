from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'
    TYPE_CHOICES = [
        (INCOME, 'Доход'),
        (EXPENSE, 'Расход'),
    ]

    ttype = models.CharField('Тип', max_length=7, choices=TYPE_CHOICES)
    amount = models.DecimalField('Сумма', max_digits=12, decimal_places=2)
    category = models.CharField('Категория', max_length=100)
    description = models.TextField('Описание', blank=True)
    date = models.DateField('Дата', default=timezone.localdate)

    class Meta:
        ordering = ['-date', '-id']
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        sign = '+' if self.ttype == self.INCOME else '-'
        return f"{self.get_ttype_display()} {sign}{self.amount} {self.category} {self.date}"
