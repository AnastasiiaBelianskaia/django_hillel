from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, help_text='Enter your first name')
    last_name = models.CharField(max_length=100, help_text='Enter your last name')
    email = models.EmailField(max_length=100, help_text='Enter your email')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
