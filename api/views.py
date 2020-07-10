from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser

from .models import Entry, Topic
from .permissions import IsOwner
from .serializers import EntrySerializer, TopicSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows entries to be viewed or edited.
    """
    queryset = Entry.objects.all()
    permission_classes = (IsOwner,)
    serializer_class = EntrySerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Entry.objects.filter(author=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows topics to be viewed or edited.
    """
    queryset = Topic.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = TopicSerializer
