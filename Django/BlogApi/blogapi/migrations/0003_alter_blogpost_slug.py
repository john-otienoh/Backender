# Generated by Django 5.1.1 on 2025-04-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapi", "0002_blogpost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="slug",
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]
