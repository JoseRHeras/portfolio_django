# Generated by Django 3.1.2 on 2020-10-22 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201022_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_info',
            old_name='github_link',
            new_name='github_link_url',
        ),
        migrations.RenameField(
            model_name='contact_info',
            old_name='linked_in',
            new_name='linked_in_url',
        ),
    ]
