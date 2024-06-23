from django.db import models
from .validators import real_age


class Birthday(models.Model):
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
        verbose_name='Дата рождения',
        validators=(real_age,)
        )

    class Meta:
        verbose_name = 'День рождения'
        verbose_name_plural = 'Дни рождений'

    def __str__(self):
        return self.first_name
