from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Client, EmailAuthToken, User
from .serializers import ClientListSerializer, UserCreateSerializer


class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer


def activate_user(request, token, user_id):
    user = User.objects.get(pk=user_id)
    token_obj = EmailAuthToken.objects.get(user=user)
    if token == token_obj.token:
        user.is_active = True
        user.save(update_fields=['is_active'])
        token_obj.delete()
        return HttpResponse('Success!')
    else:
        return HttpResponse('Token is not valid!')
