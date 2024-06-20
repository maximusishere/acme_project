from django.db import models


class BirthdayForm(models.Model):
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=20,
        blank=False
        )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=40,
        blank=True,
        help_text="Необязательное поле"
        )
    birthday = models.DateField(
        blank=False,
        verbose_name='Дата рождения'
        )
