from django.contrib import admin
from .models import Collection, Picture


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'created')

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Обложка'
    image_preview.allow_tags = True


class PictureAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'collection', 'created')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Изображение'
    image_preview.allow_tags = True


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Picture, PictureAdmin)
