from django.contrib import admin
from app.models import Mess, SendTo


@admin.register(Mess)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(SendTo)
class ToAdmin(admin.ModelAdmin):
    pass
