# Generated by Django 2.1.4 on 2020-01-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_image_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='comment',
            new_name='break_down',
        ),
        migrations.AddField(
            model_name='image',
            name='key_point',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='theme',
            field=models.TextField(blank=True),
        ),
    ]
