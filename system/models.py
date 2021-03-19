from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Fundraising(models.Model):

    title = models.CharField("Мероприятие для сбора средств", max_length=255)
    description = models.TextField(blank=True, null=True)
    opening_date = models.DateTimeField("Дата начала сбора", default=timezone.now)
    closing_date = models.DateTimeField("Дата окончания сбора")
    participants = models.ManyToManyField(User, verbose_name="Участники")
    amount = models.IntegerField("Сумма", default=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сбор"
        verbose_name_plural = "Сборы"


class Fee(models.Model):

    user = models.OneToOneField(User, verbose_name="Плательщик", on_delete=models.CASCADE)
    fundraising = models.ForeignKey(Fundraising, verbose_name="Событие", on_delete=models.CASCADE)
    date = models.DateTimeField("Дата оплаты", default=timezone.now)
    amount = models.IntegerField("Сумма", null=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
