import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe


# Create your models here.
class Collection(models.Model):
    title = models.CharField('Название', max_length=256, help_text='Введите название коллекции')
    cover_picture = models.ImageField('Обложка', upload_to='images/', help_text='Добавьте обложку для коллекции')
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    @property
    def image_preview(self):
        return mark_safe(
            f'<img style="display: block; max-width: 230px; max-height: 80px; width: auto, height: auto;" src="{self.cover_picture.url}">')

    def __str__(self):
        return self.title


class Picture(models.Model):
    image = models.ImageField('Изображение', upload_to='images/', help_text='Добавьте изображение в коллекцию')
    collection = models.ForeignKey(Collection, verbose_name='Коллекция', on_delete=models.CASCADE,
                                   help_text='Выберите коллекцию, к которой принадлежит изображение')
    created = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    @property
    def image_preview(self):
        return mark_safe(
            f'<img style="display: block; max-width: 230px; max-height: 80px; width: auto, height: auto;" src="{self.image.url}">')


@receiver(models.signals.post_delete, sender=Collection)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.cover_picture:
        if os.path.isfile(instance.cover_picture.path):
            os.remove(instance.cover_picture.path)


@receiver(models.signals.pre_save, sender=Collection)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Collection.objects.get(pk=instance.pk).cover_picture
    except Collection.DoesNotExist:
        return False

    new_file = instance.cover_picture
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(models.signals.post_delete, sender=Picture)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Picture)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Picture.objects.get(pk=instance.pk).image
    except Picture.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
