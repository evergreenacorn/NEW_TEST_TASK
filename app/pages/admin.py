from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from . import models


# Register your models here.
for model in (
    models.Page,
    models.ContentTypeVideo,
    models.ContentTypeAudio,
    models.ContentTypeText
):
    admin.site.register(model, SimpleHistoryAdmin)
