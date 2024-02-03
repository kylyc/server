from django.db import models

# Create your models here.
class TelegramUsers(models.Model):
    id_user = models.CharField(
        max_length=100,
        verbose_name="ID пользователя"
    )
    username = models.CharField(
        max_length=100,
        verbose_name="Никнейм пользователя",
        blank=True, null=True
    )
    fullname = models.CharField(
        max_length=100,
        verbose_name="Никнейм пользователя",
        blank=True, null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        return f"имя - {self.fullname}"
    
    class Meta:
        verbose_name="Пользователь телеграмма"
        verbose_name_plural="Пользователи телеграмма"