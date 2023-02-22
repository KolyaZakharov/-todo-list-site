from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from tasks.models import Task, Tag

TASK_URL = reverse("tasks:index")


class FixtureListTests(TestCase):
    def test_get_fixture_data(self):
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(list(response.context["task_list"]), [])
        self.assertEqual(len(list(response.context["task_list"])), 2)


class OwnTaskTests(TestCase):
    def test_get_own_data(self):
        self.task = Task.objects.create(
            content="test content", is_complete=False, datetime=datetime.now()
        )
        all_tasks = Task.objects.all()
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual((list(all_tasks)), list(all_tasks))


class TaskTagsTests(TestCase):
    def setUp(self) -> None:
        self.task_tag_one = Tag.objects.create(name="test tag one")
        self.task_tag_two = Tag.objects.create(name="test tag two")

    def test_get_tags(self):
        self.task = Task.objects.create(
            content="test", is_complete=False, datetime=datetime.now()
        )
        self.task.tag.add(self.task_tag_one, self.task_tag_two)
        response = self.client.get(TASK_URL)

        self.assertEqual(
            list(response.context["task_list"].filter(content="test").first().tag.all()),
            list(self.task.tag.all()),
        )