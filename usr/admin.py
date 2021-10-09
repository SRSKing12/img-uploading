from django.contrib import admin
from .models import Userinfo

# Register your models here.
@admin.register(Userinfo)
class UserDisp(admin.ModelAdmin):
    list_display=['id', 'full_Name', 'phone','state', 'date']