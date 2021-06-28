from rest_framework import serializers
from .models import Page, ContentTypeVideo, ContentTypeAudio, ContentTypeText


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"


class ContentTypeVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentTypeVideo
        fields = "__all__"


class ContentTypeAudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentTypeAudio
        fields = "__all__"


class ContentTypeTextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentTypeText
        fields = "__all__"
