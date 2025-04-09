from django.core.exceptions import ValidationError


def name_validator(name):
    if not name.isalpha():
        raise ValidationError('Fruit name should contain only letters!')