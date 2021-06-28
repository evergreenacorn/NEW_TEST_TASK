from django.contrib import admin
from django.contrib.auth.models import User, Group
from simple_history.admin import SimpleHistoryAdmin
from .models import (
    _, Page, ContentTypeVideo,
    ContentTypeAudio, ContentTypeText
)


# Register your models here.
admin.site.site_header = _("TEST TASK Admin")
admin.site.site_title = _("TEST TASK Admin Portal")
admin.site.index_title = _("Welcome to the admin panel of the TEST TASK project!")


for model in (
    Page,
    ContentTypeVideo,
    ContentTypeAudio,
    ContentTypeText
):
    admin.site.register(model, SimpleHistoryAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
