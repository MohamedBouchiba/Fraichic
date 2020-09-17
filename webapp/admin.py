from django.contrib import admin
from webapp.models import User, Products


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Products)

admin.site.register(User, UserAdmin)
