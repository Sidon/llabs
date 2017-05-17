from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from core.models import Person


class PersonTest(APITestCase):

    url = reverse('person-list')
    data = {'facebookId': '4'}

    def setUp(self):
        self.username = "admin"
        self.email = ""
        self.password = "master.21"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_insert_person(self):

        response = self.client.post(self.url, self.data )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().facebookId, 4)


# @todo | Criar mais alguns testescase