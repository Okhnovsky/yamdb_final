from django.core.exceptions import ValidationError
from datetime import date


def validate_year(value):
    if value > date.today().year:
        raise ValidationError(
            ('Год не может быть больше текущего: значение %(value)s не верно'),
            params={'value': value}
        )
