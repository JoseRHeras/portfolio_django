# Generated by Django 3.1.2 on 2020-11-12 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_paragraphimage_leading'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleparagraph',
            name='carousel_name',
            field=models.TextField(default='carousel-default', max_length=30),
        ),
    ]
