# Generated by Django 3.0.5 on 2020-05-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_wishlist', '0008_auto_20200512_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
