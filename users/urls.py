from django.urls import path

from .views import ClientListView, UserCreateView, activate_user

urlpatterns = [
    path('users/create/', UserCreateView.as_view()),
    path('users/create/activate/<uuid:token>/<int:user_id>/', activate_user),
    path('clients/', ClientListView.as_view()),
]
