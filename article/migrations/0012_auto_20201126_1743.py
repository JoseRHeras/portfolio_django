# Generated by Django 3.1.2 on 2020-11-26 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20201126_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullarticle',
            name='article_brief',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article'),
        ),
    ]