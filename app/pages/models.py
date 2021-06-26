from django.db import models
from datetime.datetime import now
from django.contrib.auth import User


# Create your models here.
class RecordInfo(models.Model):
    """
    Абстрактная модель
    Информация о создании/обновлении записи

    Аргументы:
        title (CharField(255)):     Название
        created_at (DateTimeField): Дата создания
        udated_at (DateTimeField):  Дата модификации
        created_by (ForeignKey):    Создано пользователем
        updated_by (ForeignKey):    Обновлено пользователем
    """
    title =      models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User)
    updated_by = models.ForeignKey(User)

    class Meta:
        abstract = True


class ViewInfo(models.Model):
    """Абстрактная модель
    Информация о просмотрах

    Аргументы:
        view_counter (IntegerField): Кол-во просмотров
    """
    view_counter = models.IntegerField()

    class Meta:
        abstract = True


class Page(ModelInfo):
    """
    Модель Страница
    Аргументы:
        slug (SlugField(160)):  Слаг-поле
    """
    slug = models.SlugField(max_length=160, unique=True)


# class ContentTypeVideo(ModelInfo, ViewInfo):
#     file_link = models
#     subtitles_file_link


# class ContentTypeAudio(ModelInfo, ViewInfo):
#     file_link
#     bitrate


# class ContentTypeText(ModelInfo, ViewInfo):
#     text
