# Generated by Django 3.0.7 on 2020-07-06 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_students_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
