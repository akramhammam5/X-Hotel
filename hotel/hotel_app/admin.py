from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ContactMessage)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')