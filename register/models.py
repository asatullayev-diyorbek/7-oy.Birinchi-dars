import random
import string

from django.db import models


class Confirmation(models.Model):
    email = models.CharField(max_length=150)
    confirmation_code = models.CharField(max_length=6)

    def __str__(self):
        return f"Confirmation code for {self.email}"

    class Meta:
        verbose_name = "Confirmation code"
        verbose_name_plural = "Confirmation codes"

    @staticmethod
    def generate_confirmation_code():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

