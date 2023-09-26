from django.db import models

from customers.models import Customer


class Order(models.Model):
    id = models.AutoField(
        primary_key=True,
        default=1
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    robot_serial = models.CharField(
        max_length=5,
        blank=False,
        null=False
    )
