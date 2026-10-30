from rest_framework.test import APITestCase
from rest_framework import status

from .models import Task


class TaskAPITests(APITestCase):

    def test_get_tasks(self):
        response = self.client.get("/api/tasks/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_create_task(self):
        data = {
            "title": "Learn Django",
            "description": "Practice API testing",
            "status": "pending",
            "priority": "high",
        }

        response = self.client.post(
            "/api/tasks/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.get()
        self.assertEqual(task.priority, "high")

    def test_create_task_with_invalid_status(self):
        data = {
            "title": "Bad task",
            "description": "This should fail",
            "status": "banana",
            "priority": "high",
        }

        response = self.client.post(
            "/api/tasks/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        self.assertEqual(Task.objects.count(), 0)
from rest_framework.test import APITestCase
from rest_framework import status


class TaskAPITests(APITestCase):

    def test_tasks_require_authentication(self):
        response = self.client.get("/api/tasks/")

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

def test_user_cannot_access_another_users_task(self):
    another_user = User.objects.create_user(
        username="anotheruser",
        password="password123",
    )

    another_task = Task.objects.create(
        title="Private task",
        description="Another user's task",
        owner=another_user,
    )

    response = self.client.get(
        f"/api/tasks/{another_task.id}/"
    )

    self.assertEqual(
        response.status_code,
        status.HTTP_404_NOT_FOUND,
    )