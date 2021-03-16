import uuid

from django.conf import settings
from django.core.mail import send_mail

from .models import EmailAuthToken


def send_auth_token_to_email(user_obj):
    token = uuid.uuid4()
    activate_url = f'http://127.0.0.1:8000/api/v1/users/create/access/{token}/{user_obj.pk}'
    EmailAuthToken.objects.create(user=user_obj, token=token)
    message = f'Ссылка для активаций аккаунта: {activate_url}'
    send_mail('Email verification for django', message, settings.EMAIL_HOST_USER, [user_obj.email])
