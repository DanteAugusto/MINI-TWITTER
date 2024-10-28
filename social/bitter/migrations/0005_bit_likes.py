# Generated by Django 5.1.2 on 2024-10-28 00:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitter', '0004_profile_profile_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bit',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='bit_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
