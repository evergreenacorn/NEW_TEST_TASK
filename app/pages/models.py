from django.db import models
from datetime.datetime import now
from django.contrib.auth import User
from django.utils.translation import gettext_lazy as _


CONTENTTYPES_DIRS = {
    "video_file": {
        "remote": "contenttypes/video/files/remote/",
        "local": "contenttypes/video/files/local/"
    },
    "video_subtitles": {
        "remote": "contenttypes/video_subtitles/files/remote/",
        "local": "contenttypes/video_subtitles/files/local/"
    },
    "audio_file": {
        "remote": "contenttypes/audio/files/remote/",
        "local": "contenttypes/audio/files/local/"
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
        upload_to=None,
        null=True,
        blank=True
    )
    video_file_link = models.URLField(
        _("Remote video file"),
        max_length=500,
        upload_to=None,
        null=True,
        blank=True
    )
    subtitles_file_path = models.FileField(
        _("Local subtitles file"),
        upload_to=None,
        null=True,
        blank=True
    )
    subtitles_file_link = models.URLField(
        _("Remote subtitles file"),
        max_length=500,
        upload_to="contenttypes/video/subtitles/%s/%s/%Y-%m-%d/" % (
            self.created_by.username, self.title
        ),
        null=True,
        blank=True
    )

    def clean(self):
        """Вызываем ValidationError, если указана ссылка
        как на локальный файл, так и на удаленный
        """
        pass

    @classmethod
    def user_directory_path(cls):
        return ''

# class ContentTypeAudio(ModelInfo, ViewInfo):
#     file_link
#     bitrate


# class ContentTypeText(ModelInfo, ViewInfo):
#     text
