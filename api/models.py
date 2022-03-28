import os

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomAccountManager(BaseUserManager):

    def _create_user(self, email, password, is_active, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, is_active=True, is_staff=False, is_superuser=False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, is_active=True, is_staff=True, is_superuser=True, **extra_fields)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта', unique=True)
    first_name = models.CharField('Имя', max_length=15, blank=True, null=True)
    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
    is_staff = models.BooleanField('Администратор', default=False)
    is_active = models.BooleanField('Активен', default=True)
    is_superuser = models.BooleanField('Суперадмин', default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Collection(models.Model):
    title = models.CharField('Название', max_length=256, help_text='Введите название коллекции')
    cover_picture = models.ImageField('Обложка', upload_to='images/', help_text='Добавьте обложку для коллекции')
    created = models.DateTimeField('Дата создания коллекции', auto_now_add=True)

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
    created = models.DateTimeField('Дата добавления изображения', auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    @property
    def image_preview(self):
        return mark_safe(
            f'<img style="display: block; max-width: 230px; max-height: 80px; width: auto, height: auto;" src="{self.image.url}">')

    def __str__(self):
        return f'Изображение из коллекции {self.collection}'


class Service(models.Model):
    title = models.CharField('Название', max_length=256, help_text='Введите название услуги')
    description = models.TextField('Описание', help_text='Введите описание услуги')
    price = models.PositiveIntegerField('Цена', help_text='Введите цену услуги')

    class Meta:
        ordering = ['title']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.TextField('Содержимое отзыва', help_text='Введите содержимое отзыва')
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    created = models.DateTimeField('Дата создания отзыва', auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыва пользователя {self.user.first_name} ({self.user.email})'


class Order(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, verbose_name='Услуга', on_delete=models.CASCADE)
    is_accepted = models.BooleanField('Принят в обработку', default=False)
    is_completed = models.BooleanField('Выполнен', default=False)
    created = models.DateTimeField('Дата создания заказа', auto_now_add=True)
    time_accepted = models.DateTimeField('Дата принятия в обработку', blank=True, null=True)
    time_completed = models.DateTimeField('Дата выполнения', blank=True, null=True)

    def accept(self):
        self.is_accepted = True
        self.time_accepted = timezone.now()

    def complete(self):
        self.is_accepted = False
        self.is_completed = True
        self.time_completed = timezone.now()

    class Meta:
        ordering = ['-created']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ услуги "{self.service.title} от пользователя {self.user.first_name} ({self.user.email})"'


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
