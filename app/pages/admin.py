from django.contrib import admin
from . import models


# Register your models here.
for model in (
    models.Page,
    models.ContentTypeVideo,
    models.ContentTypeAudio,
    models.ContentTypeText
):
    admin.site.register(model)
