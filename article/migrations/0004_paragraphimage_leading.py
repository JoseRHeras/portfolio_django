# Generated by Django 3.1.2 on 2020-11-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_paragraphimage_alt_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraphimage',
            name='leading',
            field=models.BooleanField(default=False),
        ),
    ]