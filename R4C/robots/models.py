from django.db import models

from .validators import validate_length


class RobotModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=2,
        unique=True,
        blank=False,
        null=False,
        validators=[validate_length]
    )

    def __str__(self):
        return self.name


class Robot(models.Model):
    id = models.AutoField(
        primary_key=True,
        default=1
    )
    model = models.ForeignKey(
        RobotModel,
        on_delete=models.CASCADE
    )
    version = models.CharField(
        max_length=2,
        blank=False,
        null=False,
        validators=[validate_length]
    )
    created = models.DateTimeField(
        blank=False,
        null=False
    )
    serial = models.CharField(
        max_length=6,
        blank=True,
        null=False
    )

    def save(self, *args, **kwargs):
        """
        Генерируем значение для поля 'serial' на основе 'model' и 'version'.
        """
        self.serial = f"{self.model.name}-{self.version}"
        super(Robot, self).save(*args, **kwargs)
