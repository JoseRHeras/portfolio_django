# Generated by Django 3.1.2 on 2020-11-12 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20201110_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraphimage',
            name='alt_description',
            field=models.CharField(default='image', max_length=50),
        ),
    ]