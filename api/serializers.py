from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from .models import Topic, Entry


class EntrySerializer(serializers.ModelSerializer):
    topic = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Topic.objects.all()
    )

    class Meta:
        model = Entry
        fields = ('id', 'title', 'topic', 'created_at', 'updated_at', 'content')


class TopicSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(
        many=True,
        required=False
    )

    class Meta:
        model = Topic
        fields = ('id', 'name', 'description', 'entries')
