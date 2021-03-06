import jwt
from django.conf import settings
from vuelosApp.models.user import User
from rest_framework import status
from rest_framework.test import APITestCase


class TestAPI(APITestCase):
    
    def test_signUp(self):
        previos_user_count = User.objects.all().count()
        new_user = {
            "username": "user1",
            "password": "pass1",
            "first_name": "Usuario1",
            "last_name": "Usuario1",
            "email": "user1@misiontic.com",   
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
        self.assertEqual('refresh' in response.data.keys(), True)
        self.assertEqual('access' in response.data.keys(), True)
        self.assertEqual(User.objects.all().count(), previos_user_count + 1)

    def test_login(self):
        user = {
            "username": "Papo20",
            "password": "contraseña"
        }
        response = self.client.post(
            '/login/',
            user,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('refresh' in response.data.keys(), True)
        self.assertEqual('access' in response.data.keys(), True)

    def authenticate(self):
        token_access = self.client.post(
            '/login/',
            {
                "username": "pepito89",
                "password": "micontraseña"
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
        self.assertEqual(response.data["username"], "pepito89")

    def test_reservacreateview(self):
        id_user = self.authenticate()
        new_reservation = {
            "cliente": id_user,
            "vuelo": 1,
            "puestos": 2
        }
        response = self.client.post(
            '/reserva/create/',
            new_reservation,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_reservalistview(self):
        id_user = self.authenticate()
        response = self.client.get(
            '/reserva/list/{}'.format(id_user)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)