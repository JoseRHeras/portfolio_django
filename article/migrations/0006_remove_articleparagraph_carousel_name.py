# Generated by Django 3.1.2 on 2020-11-12 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_articleparagraph_carousel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleparagraph',
            name='carousel_name',
        ),
    ]
