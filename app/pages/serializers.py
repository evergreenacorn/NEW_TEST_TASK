from rest_framework import serializers
from .models import Page, ContentTypeVideo, ContentTypeAudio, ContentTypeText


class AbstractContentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"


class ContentTypeVideoSerializer(AbstractContentTypeSerializer):
    class Meta(AbstractContentTypeSerializer.Meta):
        model = ContentTypeVideo


class ContentTypeAudioSerializer(AbstractContentTypeSerializer):
    class Meta(AbstractContentTypeSerializer.Meta):
        model = ContentTypeAudio


class ContentTypeTextSerializer(AbstractContentTypeSerializer):
    class Meta(AbstractContentTypeSerializer.Meta):
        model = ContentTypeText


class PageSerializer(serializers.HyperlinkedModelSerializer):
    videos = ContentTypeVideoSerializer(source="page_videos", many=True)
    audios = ContentTypeAudioSerializer(source="page_audios", many=True)
    texts = ContentTypeTextSerializer(source="page_texts", many=True)

    class Meta:
        model = Page
        fields = "__all__"
