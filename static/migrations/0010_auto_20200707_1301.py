# Generated by Django 3.0.7 on 2020-07-07 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_students_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name': 'stds'},
        ),
        migrations.AlterModelTable(
            name='students',
            table='stds',
        ),
    ]