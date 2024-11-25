from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Task.objects.create(
            title="First Todo",
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(str(self.todo), "First Todo")
