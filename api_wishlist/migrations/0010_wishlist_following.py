# Generated by Django 3.0.5 on 2020-05-12 16:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_wishlist', '0009_auto_20200512_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='follwed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
