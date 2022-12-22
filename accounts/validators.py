import os

from django.core.exceptions import ValidationError


def allow_only_images(value):
    ext = os.path.splitext(value.name)[1]
    print(ext)
    valid_extentions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extentions:
        raise ValidationError('Unsupported file extension. Allowed extension: ' + str(valid_extentions))
