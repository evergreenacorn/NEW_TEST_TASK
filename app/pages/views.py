from rest_framework import renderers, viewsets, generics, mixins
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import PageSerializer, ContentTypeVideoSerializer, ContentTypeAudioSerializer, ContentTypeTextSerializer
from .models import Page, ContentTypeVideo, ContentTypeAudio, ContentTypeText
# from rest_framework.decorators import detail_route
from .task import update_views_count


class AbstractReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = None
    queryset = None
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("title", "page__title")
    ordering_fields = (
        "pk", "title", "serial_number", "page_id"
    )
    paginate_by = 20


class PageModelViewset(AbstractReadOnlyViewset):
    serializer_class = PageSerializer
    queryset = Page.objects.prefetch_related("page_videos", "page_audios", "page_texts").all()
    search_fields = (
        "title",
        "page_videos__title",
        "page_audios__title",
        "page_texts__title",
    )
    ordering_fields = (
        "pk", "title",
        "page_videos__serial_number",
        "page_audios__serial_number",
        "page_texts__serial_number",
    )


class VideoModelViewset(AbstractReadOnlyViewset):
    serializer_class = ContentTypeVideoSerializer
    queryset = ContentTypeVideo.objects.select_related("page").all()


class AudioModelViewset(AbstractReadOnlyViewset):
    serializer_class = ContentTypeAudioSerializer
    queryset = ContentTypeAudio.objects.select_related("page").all()


class TextModelViewset(AbstractReadOnlyViewset):
    serializer_class = ContentTypeTextSerializer
    queryset = ContentTypeText.objects.select_related("page").all()
    search_fields = (
        "title", "^text",
    )
