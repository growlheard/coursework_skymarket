from rest_framework.test import APITestCase
from users.models import User
from .models import Ad, Comment


class AdTestCase(APITestCase):
    def setUp(self) -> None:
        """
        Подготовка данных перед тестом
        """
        self.user = User.objects.create(
            email='user@user.com',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role='user'
        )
        self.user.set_password('123')
        self.user.save()
        response = self.client.post('/login/', {"email": "user@user.com", "password": "123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_ad_create(self):
        """
        Тест создания объявления
        """
        data = {
            'title': 'test',
            'price': 100,
            'description': 'test',
            'author': self.user.id
        }
        response = self.client.post('/ads/', data)
        self.assertEqual(response.status_code, 201)

    def test_get_ad_details(self):
        """
        Тест получения деталей объявления
        """
        ad = Ad.objects.create(
            title='test',
            price=100,
            description='test',
            author=self.user
        )
        response = self.client.get(f'/ads/{ad.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_create_comment(self):
        """
        Тест создания комментария
        """
        ad = Ad.objects.create(
            title='test',
            price=100,
            description='test',
            author=self.user
        )
        data = {
            'text': 'test comment',
            'author': self.user.id,
            'ad': ad.id
        }
        response = self.client.post(f'/ads/{ad.pk}/comments/', data)
        self.assertEqual(response.status_code, 201)

    def test_get_comment_details(self):
        """
        Тест получения деталей комментария
        """
        ad = Ad.objects.create(
            title='test',
            price=100,
            description='test',
            author=self.user
        )
        comment = Comment.objects.create(
            text='test comment',
            author=self.user,
            ad=ad
        )
        response = self.client.get(f'/ads/{ad.pk}/comments/{comment.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_create_ad_invalid_data(self):
        """
        Тест создания объявления с некорректными данными
        """
        data = {
            'title': '',
            'price': 'abc',
            'description': 'test',
            'author': self.user.id
        }
        response = self.client.post('/ads/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_ad_details_not_found(self):
        """
        Тест получения деталей несуществующего объявления
        """
        response = self.client.get('/ads/9999/')
        self.assertEqual(response.status_code, 404)

    def test_create_comment_invalid_data(self):
        """
        Тест создания комментария с некорректными данными
        """
        ad = Ad.objects.create(
            title='test',
            price=100,
            description='test',
            author=self.user
        )
        data = {
            'text': '',
            'author': self.user.id,
            'ad': ad.id
        }
        response = self.client.post(f'/ads/{ad.pk}/comments/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_comment_details_not_found(self):
        """
        Тест получения деталей несуществующего комментария
        """
        ad = Ad.objects.create(
            title='test',
            price=100,
            description='test',
            author=self.user
        )
        response = self.client.get(f'/ads/{ad.pk}/comments/9999/')
        self.assertEqual(response.status_code, 404)
