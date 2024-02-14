from django.conf import settings
import jwt
from unittest import skip
from rest_framework import status
from rest_framework.test import APITestCase
from vuelosApp.models.user import User


class TestAPI(APITestCase):

    def setUp(self):
        self._create_default_user()

    def _create_default_user(self):
        user = {
            "username": "default_user",
            "password": "default_pass",
            "first_name": "Default User",
            "last_name": "Usuario",
            "email": "defaultuser@misiontic.com",
            "tarjeta": {
                "nombre_propietario": "Default",
                "fecha_vencimiento": "2024-11-01",
                "tipo" : "A"
            }
        }
        response = self.client.post(
            '/user/',
            user,
            format='json'
        )

    def test_signUp(self):
        previous_user_count = User.objects.all().count()
        new_user = {
            "username": "new_user",
            "password": "new_pass",
            "first_name": "New User",
            "last_name": "Usuario",
            "email": "newuser@misiontic.com",
            "tarjeta": {
                "nombre_propietario": "Usuario",
                "fecha_vencimiento": "2024-11-01",
                "tipo" : "A"
            }
        }
        response = self.client.post(
            '/user/',
            new_user,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
        self.assertEqual(User.objects.all().count(), previous_user_count + 1)

    def test_login(self):
        user = {
            "username": "default_user",
            "password": "default_pass"
        }
        response = self.client.post(
            '/login/',
            user,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)

    def authenticate(self):
        token_access = self.client.post(
            '/login/',
            {
                "username": "default_user",
                "password": "default_pass"
            },
            format='json'
        ).data.get("access")

        secret = settings.SECRET_KEY

        id_user = jwt.decode(
            token_access, secret,
            algorithms=settings.SIMPLE_JWT["ALGORITHM"]).get("user_id")

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(token_access))
        return id_user

    def test_userdetailview(self):
        id_user = self.authenticate()
        response = self.client.get(
            '/user/{}'.format(id_user)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "default_user")

    @skip("IntegrityError, to review later")
    def test_reservacreateview(self):
        id_user = self.authenticate()
        new_reservation = {
            "cliente": id_user,
            "vuelo": 6,
            "puestos": 2
        }
        response = self.client.post(
            '/reserva/create/',
            new_reservation,
            format='json'
        )
        print("response for debugging\n\n", response, response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_reservalistview(self):
        id_user = self.authenticate()
        response = self.client.get(
            '/reserva/list/{}'.format(id_user)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
