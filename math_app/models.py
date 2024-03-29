from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Person(models.Model):
    first_name = models.CharField(max_length=100, help_text='Enter your first name')
    last_name = models.CharField(max_length=100, help_text='Enter your last name')
    email = models.EmailField(max_length=100, help_text='Enter your email')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Logs(models.Model):
    GET = 'GET'
    POST = 'POST'
    request_type_choices = [
        (GET, 'GET'),
        (POST, 'POST'),
    ]

    path = models.CharField(max_length=200)
    method = models.CharField(max_length=4, choices=request_type_choices)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    data = models.JSONField()

    def __str__(self):
        return f'{self.user} {self.data}'
