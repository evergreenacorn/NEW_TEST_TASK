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


class PageModelViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.prefetch_related("page_videos", "page_audios", "page_texts").all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = (
        "title",
        "page_videos__title",
        "page_audios__title",
        "page_texts__title",
        "=page_texts__text",  # матчим текст в контенте текста
    )
    ordering_fields = (
        "pk", "title",
    )
    paginate_by = 20


class VideoModelViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContentTypeVideoSerializer
    queryset = ContentTypeVideo.objects.all()
    paginate_by = 20
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = (
        "title", "page__title"
    )
    ordering_fields = (
        "pk", "title", "serial_number", "page__pk"
    )


class AudioModelViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContentTypeAudioSerializer
    queryset = ContentTypeAudio.objects.all()
    paginate_by = 20
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = (
        "title", "page__title"
    )
    ordering_fields = (
        "pk", "title", "serial_number", "page__pk"
    )


class TextModelViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContentTypeTextSerializer
    queryset = ContentTypeText.objects.all()
    paginate_by = 20
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = (
        "title", "page__title", "=text"
    )
    ordering_fields = (
        "pk", "title", "serial_number", "page__pk"
    )
