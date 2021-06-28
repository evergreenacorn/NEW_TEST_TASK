from rest_framework import renderers, viewsets, generics
from rest_framework import permissions
from .serializers import PageSerializer
from .models import Page, ContentTypeVideo, ContentTypeAudio, ContentTypeText


class PageListDetailView(viewsets.ModelViewSet):
    # model = Page
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    paginate_by = 20
