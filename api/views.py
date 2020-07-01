from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Entry, Topic
from .serializers import EntrySerializer, TopicSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows entries to be viewed or edited.
    """
    queryset = Entry.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EntrySerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows topics to be viewed or edited.
    """
    queryset = Topic.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TopicSerializer
