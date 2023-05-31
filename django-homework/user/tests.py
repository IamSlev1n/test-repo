import random
import factory
from django.test import TestCase
from .models import User


# Create your tests here.

class RandomUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(1, 100)

    class Meta:
        model = User


class AdultUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(18, 100)

    class Meta:
        model = User


class YoungUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(1, 17)

    class Meta:
        model = User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()
        cls.adult_user = AdultUserFactory.create()
        cls.young_user = YoungUserFactory.create()

    def test_user(self):
        self.assertIsInstance(self.user, User)

    def test_user_age(self):
        self.assertIsNotNone(self.user.age)

    def test_adult_user(self):
        self.assertTrue(self.adult_user.is_adult())
        self.assertFalse(self.young_user.is_adult())


class UserViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()

    def test_user_list(self):
        resp = self.client.get(f'/users/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('count'), 1)
        random_number = random.randint(1, 10)
        for _ in range(random_number):
            RandomUserFactory.create()
        resp = self.client.get(f'/users/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('count'), random_number + 1)

    def test_user_create(self):
        user_data = {
            'first_name': 'Created',
            'last_name': 'User',
            'age': 1
        }
        resp = self.client.post('/users/', data=user_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json().get('first_name'), user_data.get('first_name'))

    def test_get_user_detail(self):
        resp = self.client.get(f'/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('first_name'), self.user.first_name)

    def test_user_delete(self):
        resp = self.client.delete(f'/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 204)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())
