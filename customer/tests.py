import json
from django.test import TestCase
from django.urls import reverse
from .models import User



class TestRegisterLogin(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(username='ali@gmail.com',
                                 email='ali@gmail.com',
                                 user_type='customer',
                                 first_name='ali',
                                 last_name='gach',
                                 phone=9199887402,
                                 password='1234')

    def test_register_user(self):
        request_data = {'username': 'ali@gmail.com',
                        'first_name': 'ali',
                        'last_name': 'gach',
                        'phone': 9199887402,
                        'password1': '1234',
                        'password2': '1234'}
        response = self.client.post(reverse('register_login'), data=request_data)

        assert response.data.get('msg') and response.data.get('msg') == "User created successfully"
        # existing username request
        request_data_2 = {'username': 'ali@gmail.com',
                        'first_name': 'ali',
                        'last_name': 'gach',
                        'phone': 9199887402,
                        'password1': '1234',
                        'password2': '1234'}
        response_2 = self.client.post(reverse('register_login'), data=request_data_2)
        assert response_2.data.get('msg') and response_2.data.get('msg') == "This emial is taken"

    def test_login(self):
        request_data = {"username": "mohammad49517879@gmail.com", "password": "1234"}

        response = self.client.put(reverse('register_login'), data=request_data, content_type='application/json')
        assert response.data.get('token')

        request_data2 = {'username': 'ali@gmail.com',
                         'password': '1234'}
        response2 = self.client.put(reverse('register_login'), data=request_data2, content_type='application/json')
        assert not response2.data.get('token')

# Create your tests here.
