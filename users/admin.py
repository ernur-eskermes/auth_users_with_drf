from django.contrib import admin

from .models import Client, EmailAuthToken


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(EmailAuthToken)
class EmailAuthTokenAdmin(admin.ModelAdmin):
    list_display = ('user',)
