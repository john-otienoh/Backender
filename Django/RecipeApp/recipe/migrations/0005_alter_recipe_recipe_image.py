# Generated by Django 5.1.1 on 2025-03-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_images'),
        ),
    ]
