from django.utils.translation import gettext_lazy as _
from django.contrib.auth import User
from django.core.exceptions import ValidationError
from datetime.datetime import now
from django.db import models


CONTENTTYPES_DIRS = {
    "video_file": {
        "remote": "contenttypes/video/files/remote/%Y/%m/%d/",
        "local": "contenttypes/video/files/local/%Y/%m/%d/"
    },
    "video_subtitles": {
        "remote": "contenttypes/video_subtitles/files/remote/%Y/%m/%d/",
        "local": "contenttypes/video_subtitles/files/local/%Y/%m/%d/"
    },
    "audio_file": {
        "remote": "contenttypes/audio/files/remote/%Y/%m/%d/",
        "local": "contenttypes/audio/files/local/%Y/%m/%d/"
    }
}


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
    title = models.CharField(
        _("Title"),
        max_length=255,
        unique=True,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(_("Created at"), default=now)
    updated_at = models.DateTimeField(_("Updated at"), null=True)
    created_by = models.ForeignKey(User, verbose_name=_("Created by user"))
    updated_by = models.ForeignKey(User, verbose_name=_("Updated by user"))

    class Meta:
        abstract = True


class ViewInfo(models.Model):
    """Абстрактная модель
    Информация о просмотрах

    Аргументы:
        view_counter (IntegerField): Кол-во просмотров
    """
    view_counter = models.IntegerField(_("Number of views"))

    class Meta:
        abstract = True


class Page(ModelInfo):
    """
    Модель Страница
    Аргументы:
        slug (SlugField(160)):  Слаг-поле
    """
    slug = models.SlugField(max_length=160, populate_from="title")

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
        unique_together = ('slug', 'title')

    def __str__(self):
        return "%s: %s" % (self.pk, self.title)


class ContentTypeVideo(ModelInfo, ViewInfo):
    """
    Модель Контент типа видео

    Аргументы:
        ModelInfo ([type]): [description]
        ViewInfo ([type]): [description]
    """
    video_file_path = models.FileField(
        _("Local video file"),
        upload_to=CONTENTTYPES_DIRS["video_file"]["local"],
        null=True,
        blank=True
    )
    video_file_link = models.URLField(
        _("Remote video file"),
        max_length=500,
        upload_to=CONTENTTYPES_DIRS["video_file"]["remote"],
        null=True,
        blank=True
    )
    subtitles_file_path = models.FileField(
        _("Local subtitles file"),
        upload_to=CONTENTTYPES_DIRS["video_subtitles"]["local"],
        null=True,
        blank=True
    )
    subtitles_file_link = models.URLField(
        _("Remote subtitles file"),
        max_length=500,
        upload_to=CONTENTTYPES_DIRS["video_subtitles"]["remote"],
        null=True,
        blank=True
    )

    def clean(self):
        """Вызываем ValidationError, если указана ссылка
        как на локальный файл, так и на удаленный
        """
        super().clean()
        if (
            (
                self.video_file_path is not None and self.video_file_link is not None
            ) or (
                self.subtitles_file_path is not None and self.subtitles_file_link
            )
        ):
            raise ValidationError(
                "Any field with postfix _path cant exists with a same prefix but with postfix _link"
            )


# class ContentTypeAudio(ModelInfo, ViewInfo):
#     file_link
#     bitrate


# class ContentTypeText(ModelInfo, ViewInfo):
#     text
