# Generated by Django 4.0.3 on 2022-04-12 16:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_order_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='user_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+79117964487', max_length=128, region=None, verbose_name='Номер телефона'),
        ),
    ]
