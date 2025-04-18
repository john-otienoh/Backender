# Generated by Django 5.1.1 on 2025-04-11 10:12

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapi", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("body", models.TextField()),
                ("publish", models.DateTimeField(default=django.utils.timezone.now)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("DF", "Draft"), ("PB", "Published")],
                        default="DF",
                        max_length=2,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Sports", "Sports"),
                            ("Technology", "Technology"),
                            ("Lifestyle", "Lifestyle"),
                        ],
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "blog_image",
                    models.ImageField(default="blog.png", upload_to="blog_images"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-publish"],
                "indexes": [
                    models.Index(
                        fields=["-publish"], name="blogapi_blo_publish_f739b0_idx"
                    )
                ],
            },
        ),
    ]
