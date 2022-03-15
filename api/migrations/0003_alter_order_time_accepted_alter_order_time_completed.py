# Generated by Django 4.0.3 on 2022-03-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_service_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_accepted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата принятия в обработку'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_completed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]
