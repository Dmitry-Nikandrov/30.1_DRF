from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """Тестирует CRUD операции с классом Lesson"""

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.course = Course.objects.create(name="Информатика", content="Информатика")
        self.lesson = Lesson.objects.create(
            name="Урок1",
            content="Урок1",
            course=self.course,
            visual=None,
            related=None,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тестирует параметры выбранного урока"""
        url = reverse("materials:lesson_get", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)
        self.assertEqual(data.get("content"), self.lesson.content)
        self.assertEqual(data.get("owner"), self.lesson.owner_id)

    def test_lesson_create(self):
        """Тестирует создание нового урока"""
        url = reverse("materials:lesson_create")
        data = {
            "name": "Урок2",
            "content": "Урок2",
            "course": self.course.pk,
            "related": "https://www.youtube.com/mail123",
        }
        response = self.client.post(url, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        """Тестирует обновление данных выбранного урока"""
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            "name": "Урок2_update",
            "content": "Урок2_update",
            "course": self.course.pk,
            "related": "https://www.youtube.com/mail124",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Урок2_update")
        self.assertEqual(data.get("content"), "Урок2_update")
        self.assertEqual(data.get("course"), 5)

    def test_lesson_delete(self):
        """Тестирует удаление выбранного урока"""
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        """Тестирует вывод списка уроков"""
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "content": self.lesson.content,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                    "related": None,
                    "visual": None,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionViewTests(APITestCase):
    """Тестирует CRUD операции с классом Subscription"""

    def setUp(self):
        self.user = User.objects.create(email="admin@mail.ru")
        self.course = Course.objects.create(
            name="Информатика", content="Информатика", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_subscribe_on(self):
        """Тестирует включение подписки"""
        self.course = Course.objects.create(
            name="Информатика", content="Информатика", owner=self.user
        )
        url = reverse("materials:sub")
        response = self.client.post(url, {"course_id": self.course.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "Подписка включена")
        self.assertTrue(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )

    def test_subscribe_off(self):
        """Тестирует отключение подписки"""
        Subscription.objects.create(user=self.user, course=self.course)
        url = reverse("materials:sub")
        response = self.client.post(url, {"course_id": self.course.pk})
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "Подписка отключена")
        self.assertFalse(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )

    def test_subscribe_course_not_found(self):
        """Тестирует несуществующий курс"""
        url = reverse("materials:sub")
        response = self.client.post(url, {"course_id": 47856})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
