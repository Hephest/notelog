from rest_framework import serializers
from .models import Topic, Entry


class EntrySerializer(serializers.ModelSerializer):
    topic = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Entry
        fields = ('name', 'topic', 'created_at', 'updated_at', 'content')


class TopicSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ('name', 'description', 'entries')
