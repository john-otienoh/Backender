# Generated by Django 5.1.1 on 2025-05-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_alter_customuser_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="avatar",
            field=models.ImageField(
                default="avatar.jpg", upload_to="profile_pictures/"
            ),
        ),
    ]
