from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.models import Entry, Topic
from api.serializers import EntrySerializer, TopicSerializer


class TopicModelTest(TestCase):

    def create_topic(self, name, description):
        return Topic.objects.create(name=name, description=description)

    def test_topic_creation(self):
        topic = self.create_topic(
            "Test topic #1",
            "First ever topic for testing purposes."
        )

        self.assertTrue(isinstance(topic, Topic))
        self.assertEqual(str(topic), topic.name)

    def test_multiple_topics_creation(self):
        first = self.create_topic(
            "Test topic #1",
            "First ever topic for testing purposes."
        )
        second = self.create_topic(
            "Test topic #2",
            "Second test topic."
        )

        self.assertTrue(isinstance(first, Topic))
        self.assertEqual(str(first), first.name)

        self.assertTrue(isinstance(second, Topic))
        self.assertEqual(str(second), second.name)

        self.assertEqual(len(Topic.objects.all()), 2)


class EntryModelTest(TestCase):

    def create_entry(self, name, content):
        topic = Topic.objects.create(
            name="Test",
            description="Test description"
        )
        return Entry.objects.create(
            name=name,
            content=content,
            topic=topic
        )

    def test_entry_creation(self):
        entry = self.create_entry(
            "Test entry #1",
            "First ever entry."
        )

        self.assertTrue(isinstance(entry, Entry))
        self.assertEqual(str(entry), entry.name)
        self.assertEqual(str(entry.topic), "Test")

    def test_multiple_entries_creation(self):
        first = self.create_entry(
            "Test entry #1",
            "First ever entry..."
        )
        second = self.create_entry(
            "Test entry #2",
            "Second test entry... maybe."
        )

        self.assertTrue(isinstance(first, Entry))
        self.assertEqual(str(first), first.name)

        self.assertTrue(isinstance(second, Entry))
        self.assertEqual(str(second), second.name)

        self.assertEqual(len(Entry.objects.all()), 2)
        self.assertEqual(len(Topic.objects.all()), 2)


class NotelogAPITestCase(TestCase):
    """Test module for Notelog API."""

    def setUp(self):
        self.client = APIClient()

    def test_api_root_exist(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_empty_topic_list(self):
        response = self.client.get(reverse('topic-list'))
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_can_get_empty_entry_list(self):
        response = self.client.get(reverse('entry-list'))
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
