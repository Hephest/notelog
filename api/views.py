from rest_framework import viewsets
from .serializers import EntrySerializer, TopicSerializer
from .models import Entry, Topic


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows entries to be viewed or edited.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows topics to be viewed or edited.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
