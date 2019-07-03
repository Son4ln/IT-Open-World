from django.core.exceptions import ValidationError
from re import match

def phone_validate(value):
    pattern = r'^([\d]+){9,12}$'
    if value:
        if not match(pattern, value):
            raise ValidationError('Vui lòng nhập đúng số điện thoại')