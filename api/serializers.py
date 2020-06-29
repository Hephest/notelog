from rest_framework import serializers
from .models import Topic, Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('name', 'created_at', 'updated_at', 'content')


class TopicSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True)

    class Meta:
        model = Topic
        fields = ('name', 'description', 'entries')
