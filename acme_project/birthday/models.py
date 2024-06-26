from django.db import models
from .validators import real_age
# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse


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
    image = models.ImageField(
        verbose_name="Фото",
        blank=True,
        upload_to='birthday_images'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
        verbose_name = 'День рождения'
        verbose_name_plural = 'Дни рождений'

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name
