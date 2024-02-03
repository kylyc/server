from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    image = models.ImageField(
        upload_to="portrait/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name="Настройки сайта"
        verbose_name_plural="Настройки сайта"

class Contact(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Имя пользователя",
        null=True, blank=True
    )
    email = models.EmailField(
        verbose_name="Почта пользователя",
        null=True, blank=True
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер телефона",
        null=True, blank=True
    )
    cause = models.CharField(
        max_length=155,
        verbose_name="Причина",
        null=True, blank=True
    )
    message = models.TextField(
        verbose_name="Сообщение",
        null=True, blank=True
    )

    def __str__(self):
        return f"имя - {self.name}"

    class Meta:
        verbose_name="Оставленный отзыв"
        verbose_name_plural="Оставленные отзывы"


class Data(models.Model):
    award = RichTextField(
        verbose_name="Кол-во наград"
    )
    project = RichTextField(
        verbose_name="Завершенные проекты"
    )
    review = RichTextField(
        verbose_name="кол-во отзывов"
    )

    def __str__(self):
        return f"{self.award}"

    class Meta:
        verbose_name="Статистика"
        verbose_name_plural="Статистика"