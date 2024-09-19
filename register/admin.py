from django.contrib import admin
from .models import Confirmation


@admin.register(Confirmation)
class ConfirmationAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'confirmation_code')
    list_display_links = ('id', 'email')

