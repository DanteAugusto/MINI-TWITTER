# Generated by Django 5.1.2 on 2024-10-27 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitter', '0003_bit'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]