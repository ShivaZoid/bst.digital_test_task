from django.core.exceptions import ValidationError


def validate_length(value):
    if len(value) != 2:
        raise ValidationError('Should be a two-character sequence.')
