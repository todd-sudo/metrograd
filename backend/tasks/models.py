from django.db import models
from django.contrib.auth.models import User


class Tenant(models.Model):
    """ Модель арендатора
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Арендатор"
        verbose_name_plural = "Арендаторы"


class Task(models.Model):
    """ Модель заявки
    """
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        verbose_name="Арендатор",
        related_name="tasks"
    )
    inn = models.PositiveBigIntegerField("ИНН")
    ogrn = models.PositiveBigIntegerField("ОГРН", null=True, blank=True)
    individual_entrepreneur = models.BooleanField("ИП", default=False)
    individual = models.BooleanField("Физ. лицо", default=False)
    egr = models.BooleanField(
        "Выписка ЕГР", default=False, null=True, blank=True
    )
    license = models.BooleanField(
        "Лицензия", default=False, null=True, blank=True
    )
    address = models.CharField("Адрес имущества", max_length=300)
    activity = models.CharField("Вид деятельности", max_length=500)
    term = models.CharField("Срок аренды", max_length=100)
    create_at = models.DateField("Дата подачи заявки", auto_now_add=True)
    fio = models.CharField("ФИО", max_length=300)
    phone = models.CharField("Телефон", max_length=15)
    passport = models.PositiveBigIntegerField("Серия и номер паспорта")

    def __str__(self):
        return f"{self.tenant.user.username}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
