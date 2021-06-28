from rest_framework import renderers, viewsets, generics
from rest_framework import permissions
from .serializers import PageSerializer, ContentTypeVideoSerializer, ContentTypeAudioSerializer, ContentTypeTextSerializer
from .models import Page, ContentTypeVideo, ContentTypeAudio, ContentTypeText


class PageModelViewset(viewsets.ModelViewSet):
    # model = Page
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    paginate_by = 20


class VideoModelViewset(viewsets.ModelViewSet):
    # model = Page
    serializer_class = ContentTypeVideoSerializer
    queryset = ContentTypeVideo.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    paginate_by = 20


class AudioModelViewset(viewsets.ModelViewSet):
    # model = Page
    serializer_class = ContentTypeAudioSerializer
    queryset = ContentTypeAudio.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    paginate_by = 20


class TextModelViewset(viewsets.ModelViewSet):
    # model = Page
    serializer_class = ContentTypeTextSerializer
    queryset = ContentTypeText.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    paginate_by = 20
