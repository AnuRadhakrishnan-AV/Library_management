# Generated by Django 4.2.14 on 2024-07-14 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libraryapp", "0012_remove_library_is_open"),
    ]

    operations = [
        migrations.AlterField(
            model_name="library",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="library_images/"),
        ),
        migrations.AlterField(
            model_name="library",
            name="librarian",
            field=models.CharField(max_length=100),
        ),
    ]
