from django.contrib import admin

from .models import Collection, Picture, CustomUser, Service, Review, Order


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'created')
    readonly_fields = ('image_preview',)

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


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'start_date')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'is_accepted', 'is_completed', 'created')


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)
