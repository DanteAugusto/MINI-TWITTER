# Generated by Django 5.1.2 on 2024-10-28 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitter', '0005_bit_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='bit',
            name='bit_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/posts/'),
        ),
    ]
