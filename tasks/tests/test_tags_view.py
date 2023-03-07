from django.test import TestCase
from django.urls import reverse

from tasks.models import Tag

TASK_URL = reverse("tasks:tags")


class DataFromFixtureListTests(TestCase):
    def test_get_fixture_data(self):
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(list(response.context["tag_list"]), [])
        self.assertEqual(len(list(response.context["tag_list"])), 4)


class OwnTagsData(TestCase):
    def test_get_fixture_data(self):
        Tag.objects.create(name="test")
        all_tags = Tag.objects.all()
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual((list(response.context["tag_list"])), list(all_tags))
