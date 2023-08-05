from django.contrib import admin

# Register your models here.
from .models import CrudUser
admin.site.register(CrudUser)