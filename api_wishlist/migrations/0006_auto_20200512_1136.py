# Generated by Django 3.0.5 on 2020-05-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_wishlist', '0005_auto_20200511_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
