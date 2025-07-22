from django.core.management.base import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = "Add all informayion"

    def handle(self, *args, **kwargs):

        User.objects.all().delete()
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Payment.objects.all().delete()

        user = User.objects.create(email="admin@mail.ru")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("1234")
        user.save()

        User1, _ = User.objects.get_or_create(
            email="ivanov@mail.ru",
            phone_number="777777777",
            password="1234",
            is_active=True,
            is_superuser=False,
            first_name="Иван",
            last_name="Иванов",
        )

        User2, _ = User.objects.get_or_create(
            email="petrov@mail.ru",
            phone_number="33333333",
            password="1234",
            is_active=True,
            is_superuser=False,
            first_name="Петр",
            last_name="Петров",
        )

        Course1, _ = Course.objects.get_or_create(
            name="Первый курс",
            content="Дальнейшее изучение школьной программы",
            owner=User1,
        )

        Course2, _ = Course.objects.get_or_create(
            name="Второй курс",
            content="Дальнейшее изучение предметов первого курса",
            owner=User2,
        )

        Lesson1, _ = Lesson.objects.get_or_create(
            name="Математика",
            content="Дальнейшее изучение основ математического анализа",
            course=Course1,
            owner=User1,
        )

        Lesson2, _ = Lesson.objects.get_or_create(
            name="Информатика",
            content="Дальнейшее изучение основ ЭВМ",
            course=Course1,
        )

        Lesson3, _ = Lesson.objects.get_or_create(
            name="История",
            content="Дальнейшее изучение истории",
            course=Course1,
        )

        Lesson4, _ = Lesson.objects.get_or_create(
            name="Аналитическая химия",
            content="Детальное изучение общей и неорганической химии первого курса",
            course=Course2,
        )

        Lesson5, _ = Lesson.objects.get_or_create(
            name="Сопротивление материалов",
            content="Специализированная техническая дисциплина для инженерных специальностей",
            course=Course2,
            owner=User2,
        )

        payments = [
            {
                "user": User1,
                "payment_date": "2025-01-01",
                "lesson_payed": Lesson1,
                "payment": 10000,
                "payment_method": "наличный расчет",
            },
            {
                "user": User1,
                "payment_date": "2025-02-01",
                "lesson_payed": Lesson2,
                "payment": 15000,
                "payment_method": "перевод на счет",
            },
            {
                "user": User1,
                "payment_date": "2025-03-01",
                "lesson_payed": Lesson2,
                "payment": 17000,
                "payment_method": "перевод на счет",
            },
            {
                "user": User1,
                "payment_date": "2025-04-01",
                "lesson_payed": Lesson3,
                "payment": 20000,
                "payment_method": "наличный расчет",
            },
            {
                "user": User1,
                "payment_date": "2025-05-01",
                "course_payed": Course2,
                "payment": 250000,
                "payment_method": "перевод на счет",
            },
            {
                "user": User2,
                "payment_date": "2026-01-01",
                "course_payed": Course1,
                "payment": 300000,
                "payment_method": "наличный расчет",
            },
            {
                "user": User2,
                "payment_date": "2026-02-01",
                "course_payed": Course2,
                "payment": 450000,
                "payment_method": "перевод на счет",
            },
            {
                "user": User2,
                "payment_date": "2026-01-05",
                "lesson_payed": Lesson4,
                "payment": 7450,
                "payment_method": "перевод на счет",
            },
            {
                "user": User2,
                "payment_date": "2026-02-05",
                "lesson_payed": Lesson5,
                "payment": 9600,
                "payment_method": "наличный расчет",
            },
        ]

        for i in payments:
            payment, created = Payment.objects.get_or_create(**i)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Успешно добавлен новый платеж: {payment}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Платеж уже создан: {payment}"))
