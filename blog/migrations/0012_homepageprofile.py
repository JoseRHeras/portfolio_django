# Generated by Django 3.1.2 on 2020-11-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20201022_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name_initial', models.CharField(default=None, max_length=1)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=150)),
                ('github_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('profile_image', models.ImageField(default='default_user_pic.jpg', upload_to='home_page_pic')),
                ('about_me', models.TextField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
