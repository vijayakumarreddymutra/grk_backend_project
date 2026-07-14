
from django.core.exceptions import ValidationError
def name_filed_validator(value):
    if len(value) < 3:
        raise ValidationError("Name Field should accept atleast 3 characters")
    if len(value) > 28:
        raise ValidationError("Name Field should accept only less 28 characters")