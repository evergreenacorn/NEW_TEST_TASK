from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime
from django.db import models


CONTENTTYPES_DIRS = {
    "video_file": "contenttypes/video/files/local/%Y/%m/%d/"
    ,
    "video_subtitles": "contenttypes/video_subtitles/files/local/%Y/%m/%d/"
    ,
    "audio_file": "contenttypes/audio/files/local/%Y/%m/%d/"
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
    created_at = models.DateTimeField(_("Created at"), default=datetime.now)
    updated_at = models.DateTimeField(_("Updated at"), null=True)
    created_by = models.ForeignKey(
        User,
        verbose_name=_("Created by user"),
        on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User,
        verbose_name=_("Updated by user"),
        on_delete=models.CASCADE
    )

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


class ContenttypeSpecialOrder(models.Model):
    """Абстрактная модель для _ContentType - моделей
    для возможности назначения порядкового номера
    записи по умолчанию.

    Аргументы:
        serial_number (IntegerField): Порядковый номер
    """
    serial_number = models.IntegerField("Serial number")

    class Meta:
        abstract = True


class ContentTypeVideo(RecordInfo, ViewInfo, ContenttypeSpecialOrder):
    """
    Модель Контент типа видео

    Аргументы:
        ModelInfo ([type]): [description]
        ViewInfo ([type]): [description]
    """
    video_file_path = models.FileField(
        _("Local video file"),
        upload_to=CONTENTTYPES_DIRS["video_file"],
        null=True,
        blank=True
    )
    video_file_link = models.URLField(
        _("Remote video file"),
        max_length=500,
        null=True,
        blank=True
    )
    subtitles_file_path = models.FileField(
        _("Local subtitles file"),
        upload_to=CONTENTTYPES_DIRS["video_subtitles"],
        null=True,
        blank=True
    )
    subtitles_file_link = models.URLField(
        _("Remote subtitles file"),
        max_length=500,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("Content type video")
        verbose_name_plural = _("Content types video")

    def __str__(self):
        return '%s: %s' % (self.pk, self.title)

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


class ContentTypeAudio(RecordInfo, ViewInfo, ContenttypeSpecialOrder):

    file_local_path = models.FileField(
        _("Local audio file"),
        upload_to=CONTENTTYPES_DIRS["audio_file"],
        null=True,
        blank=True
    )
    file_link = models.URLField(
        _("Remote audio file"),
        max_length=500,
        null=True,
        blank=True
    )
    bitrate = models.IntegerField(
        _("Bits in a second"),
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = _("Content type audio")
        verbose_name_plural = _("Content types audio")

    def __str__(self):
        return '%s: %s' % (self.pk, self.title)


class ContentTypeText(RecordInfo, ViewInfo, ContenttypeSpecialOrder):
    text = models.TextField(_("Text field"))

    class Meta:
        verbose_name = _("Content type text")
        verbose_name_plural = _("Content types text")

    def __str__(self):
        return '%s: %s' % (self.pk, self.title)


class Page(RecordInfo):
    """
    Модель Страница
    Аргументы:
        slug (SlugField(160)):  Слаг-поле
    """
    slug = models.SlugField(
        max_length=160,
        unique=True,
        # prepopulate_from=('title',)
    )
    video_content = models.ForeignKey(
        ContentTypeVideo,
        related_name="pages_video_content",
        null=True,
        blank=True,
        verbose_name="Video content",
        on_delete=models.CASCADE
    )
    audio_content = models.ForeignKey(
        ContentTypeAudio,
        related_name="pages_audio_content",
        null=True,
        blank=True,
        verbose_name="Audio content",
        on_delete=models.CASCADE
    )
    text_content = models.ForeignKey(
        ContentTypeText,
        related_name="pages_text_content",
        null=True,
        blank=True,
        verbose_name="Video content",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
        unique_together = ('slug', 'title')

    def __str__(self):
        return "%s: %s" % (self.pk, self.title)
