from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to="portrait/",
        verbose_name="Фотография для новости"
    )
    created = models.DateField(
        auto_now_add = True,
        verbose_name="Время создания",
        null=True, blank=True
    )


    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name="Новость"
        verbose_name_plural="Новости"