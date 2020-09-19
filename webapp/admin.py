from django.contrib import admin
from webapp.models import User, Products


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass


class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


admin.site.register(Products, ProductsAdmin)

admin.site.register(User, UserAdmin)
