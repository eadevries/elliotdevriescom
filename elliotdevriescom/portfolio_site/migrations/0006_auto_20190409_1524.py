# Generated by Django 2.1.5 on 2019-04-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_site', '0005_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]