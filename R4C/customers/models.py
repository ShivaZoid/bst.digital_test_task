from django.db import models


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False
    )
